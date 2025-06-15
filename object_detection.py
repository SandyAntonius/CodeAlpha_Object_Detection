from ultralytics import YOLO
import cv2

def main():

    print("Welcome, Loading YOLOv8 model...")
    model = YOLO("yolov8n.pt")
    
    video_source = 0  

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Cannot open video source!")
        return

    print("Starting object detection, if you want to quit Press 'q' ")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream.")
            break

        results = model(frame)

        # Plot detected boxes and labels
        annotated_frame = results[0].plot()

        # Show result
        cv2.imshow("YOLOv8 Object Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Quitting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
