from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

results = model.train(
    data="/Users/rishi/gitnew/Object-Detector-Pen-/Pen/data.yaml",
    epochs=80,
    imgsz=640,
    batch=8,        # lower this to 4 if you run out of memory
    name="pen_detector"
)