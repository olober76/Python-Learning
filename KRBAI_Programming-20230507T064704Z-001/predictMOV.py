import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
MODEL = "C:/Users/kuhpr/Documents/Python/Python-Learning/KRBAI_Programming-20230507T064704Z-001/mhrks_yv8_v1.pt"
model = YOLO(MODEL)

# Open the video file
video_path = "C:/Users/kuhpr/Documents/Python/Python-Learning/KRBAI_Programming-20230507T064704Z-001/KRBAI_Programming/video4.MOV"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()