import cv2
import torch
import time
import os

class YOLODetector:
    def __init__(self, model_name='yolov5s', dataset_dir='dataset'):
        self.model = self.load_model(model_name)
        self.dataset_dir = dataset_dir
        self.create_dataset_directory()
    
    def load_model(self, model_name):
        return torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)
    
    def create_dataset_directory(self):
        if not os.path.exists(self.dataset_dir):
            os.makedirs(self.dataset_dir)
    
    def detect_objects(self, frame):
        return self.model(frame)
 
class VideoCapture:
    def __init__(self, source):
        self.source = source
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise Exception("Erro ao abrir a câmera")
    
    def get_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None
    
    def release(self):
        self.cap.release()

class ROIHandler:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir
    
    def save_roi(self, image, roi, object_name):
        x1, y1, x2, y2 = roi
        if x1 != x2 and y1 != y2:
            cropped = image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
            object_folder = os.path.join(self.dataset_dir, object_name)
            os.makedirs(object_folder, exist_ok=True)
            filename = f"{object_folder}/roi_{int(time.time())}.jpg"
            cv2.imwrite(filename, cropped)

class ObjectDetectionPipeline:
    def __init__(self, cam_ip):
        self.detector = YOLODetector()
        self.video = VideoCapture(cam_ip)
        self.roi_handler = ROIHandler(self.detector.dataset_dir)
        self.paused = False
    
    def process_frame(self):
        if self.paused:
            return None, None
        
        frame = self.video.get_frame()
        if frame is None:
            return None, None
        
        results = self.detector.detect_objects(frame)
        return frame, results.render()[0]
    
    def save_roi(self, frame, roi, object_name):
        self.roi_handler.save_roi(frame, roi, object_name)
    
    def release_resources(self):
        self.video.release()
    
    def toggle_pause(self):
        self.paused = not self.paused

if __name__ == "__main__":
    cam_ip = 'rtsp://admin:FLEXI%402022@192.168.1.15:80/cam/realmonitor?channel=11&subtype=0'
    pipeline = ObjectDetectionPipeline(cam_ip)
    
    cv2.namedWindow('YOLO Detection', cv2.WINDOW_NORMAL)
    
    try:
        while True:
            frame, processed_frame = pipeline.process_frame()
            if frame is None:
                break
            
            if processed_frame is not None:
                cv2.imshow('YOLO Detection', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord(' '):
                pipeline.toggle_pause()
    
    except KeyboardInterrupt:
        print("Processo interrompido pelo usuário.")
    finally:
        pipeline.release_resources()
        cv2.destroyAllWindows()
