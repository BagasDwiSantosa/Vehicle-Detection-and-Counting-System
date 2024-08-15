import cv2
import os
from ultralytics import YOLO

def perform_detection(frame, model):
    """Perform object detection on the frame."""
    results = model(frame)
    return results

def count_vehicles(results, desired_classes):
    """Count the number of vehicles based on the desired classes for a single frame."""
    counts = {class_id: 0 for class_id in desired_classes}

    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0])
            if class_id in desired_classes:
                counts[class_id] += 1

    return counts

def draw_bounding_boxes(frame, results, desired_classes, id_tracker):
    """Draw bounding boxes, labels, and unique IDs on the frame."""
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = int(box.cls[0])
            confidence = box.conf[0]

            if class_id in desired_classes:
                label = f'{desired_classes[class_id]} ({confidence:.2f})'
                unique_id = id_tracker[class_id].pop(0)  
                full_label = f'{label} {unique_id}'
                
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, full_label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def detect_and_display_video(video_path, output_path):
    """Detect objects in the video and save the annotated video, counting vehicles overall."""
    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Define desired classes
    desired_classes = {2: 'Car', 5: 'Bus'}

    # Initialize overall counts
    overall_counts = {class_id: 0 for class_id in desired_classes}

    # Initialize unique ID trackers
    id_tracker = {
        2: [f'C{i+1}' for i in range(1000)],  # Car IDs
        5: [f'B{i+1}' for i in range(1000)]   # Bus IDs
    }

    # Open video file
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        raise Exception(f"Error opening video file {video_path}")

    # Get video properties
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID' for .avi files
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while True:
        # Read frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            break

        # Perform detection
        results = perform_detection(frame, model)

        # Count vehicles for the current frame
        frame_counts = count_vehicles(results, desired_classes)

        # Update overall counts
        for class_id, count in frame_counts.items():
            overall_counts[class_id] += count

        # Draw bounding boxes, labels, and unique IDs
        draw_bounding_boxes(frame, results, desired_classes, id_tracker)

        # Create summary text
        summary_text = ' '.join([f'{name}: {overall_counts[class_id]}' for class_id, name in desired_classes.items()])

        # Put summary text on the frame
        cv2.putText(frame, summary_text, (10, frame_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

        # Write the frame to the output video file
        out.write(frame)

    # Release video capture and writer objects
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'path/to/your/video.mp4'  # Ganti dengan jalur video input Anda
    output_path = 'path/to/output/video.mp4'  # Ganti dengan jalur video output yang diinginkan
    detect_and_display_video(video_path, output_path)
