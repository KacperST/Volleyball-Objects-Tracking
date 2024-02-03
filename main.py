import os

import supervision as sv
import cv2
from ultralytics import YOLO

dir_path = os.path.dirname(os.path.realpath(__file__))

box_annotator = sv.BoxAnnotator(
    thickness=2,
    text_thickness=1,
    text_scale=0.5
)
model = YOLO(f"{dir_path}/best7.pt")  # build a new model from scratch

for result in model.track(source=f'{dir_path}/videos/akcja2.mp4',tracker="bytetrack.yaml",stream=True, persist=True):
    frame = result.orig_img
    detections = sv.Detections.from_ultralytics(result)
    if result.boxes.id is not None:
        detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)

    labels = [
        f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
        for _,_, confidence, class_id, tracker_id in detections
    ]
    frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)
    cv2.imshow("yolov8", frame)
    if cv2.waitKey(30) == 27:
        break



