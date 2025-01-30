import cv2
from fastapi import FastAPI
from .database import models, config

app = FastAPI()

models.Base.metadata.create_all(bind=config.engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    # RTSP stream URL
    rtsp_url = 'rtsp://admin:FLEXI%402022@192.168.1.15:80/cam/realmonitor?channel=11&subtype=0'
    
    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        print("Error: Could not open video stream")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
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
