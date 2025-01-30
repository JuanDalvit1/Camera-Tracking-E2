import cv2
from fastapi import FastAPI, Response
from starlette.responses import StreamingResponse
from .database import models, config  # Ajuste para importação relativa
import logging

app = FastAPI()

models.Base.metadata.create_all(bind=config.engine)

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/capture")
def capture_image():
    logging.info("Capture endpoint called")
    rtsp_url = 'rtsp://admin:FLEXI%402022@192.168.1.15:80/cam/realmonitor?channel=11&subtype=0'
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        logging.error("Could not open video stream")
        return {"error": "Could not open video stream"}
    
    ret, frame = cap.read()
    if not ret:
        logging.error("Could not read frame")
        return {"error": "Could not read frame"}
    
    # Process the frame (example: convert to grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Save the processed frame to a file
    cv2.imwrite('captured_image.jpg', gray_frame)
    
    cap.release()
    
    logging.info("Image captured and processed successfully")
    return {"message": "Image captured and processed successfully"}

@app.get("/video_feed")
def video_feed():
    rtsp_url = 'rtsp://admin:FLEXI%402022@192.168.1.15:80/cam/realmonitor?channel=11&subtype=0'
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        logging.error("Could not open video stream")
        return Response(content="Could not open video stream", media_type="text/plain")
    
    def generate():
        while True:
            ret, frame = cap.read()
            if not ret:
                logging.error("Could not read frame")
                break
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    return StreamingResponse(generate(), media_type='multipart/x-mixed-replace; boundary=frame')

def main():
    # RTSP stream URL
    rtsp_url = 'rtsp://admin:FLEXI%402022@192.168.1.15:80/cam/realmonitor?channel=11&subtype=0'
    
    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        logging.error("Error: Could not open video stream")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            logging.error("Error: Could not read frame")
            break
        
        # Display the frame
        cv2.imshow('RTSP Stream', frame)
        
        # Exit if ESC is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
