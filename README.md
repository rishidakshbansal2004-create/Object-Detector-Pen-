# Pen Detector 🖊️

A real-time pen detection system built with **YOLOv8** and **OpenCV**. The model is fine-tuned on a custom dataset to detect pens through a live webcam feed.

## Demo

Run `webcam.py` to see live detection through your webcam — bounding boxes and confidence scores are drawn around detected pens in real time.

## Project Overview

This project demonstrates an end-to-end object detection pipeline:

1. **Data Collection** – Collected ~120 images of pens in varied angles, backgrounds, and lighting conditions.
2. **Annotation** – Labeled images using [Roboflow](https://roboflow.com), exporting in YOLOv8 format.
3. **Training** – Fine-tuned a pretrained `yolov8n` model on the custom dataset.
4. **Inference** – Built a real-time webcam detection script using OpenCV.

## Results

The model was trained for 80 epochs on a custom dataset of pen images.

| Metric | Score |
|---|---|
| Precision | 0.960 |
| Recall | 0.851 |
| mAP50 | 0.926 |
| mAP50-95 | 0.522 |

## Tech Stack

- **YOLOv8** (Ultralytics) – object detection model
- **OpenCV** – webcam capture and visualization
- **Roboflow** – dataset annotation and preprocessing
- **PyTorch** – underlying deep learning framework

## Setup & Usage

### 1. Clone the repository

\`\`\`bash
git clone <your-repo-url>
cd Object-Detector-Pen-
\`\`\`

### 2. Install dependencies

\`\`\`bash
pip install ultralytics opencv-python
\`\`\`

### 3. Run live webcam detection

\`\`\`bash
python webcam.py
\`\`\`

Press `q` to quit the webcam window.

### 4. (Optional) Retrain the model

If you want to retrain on your own dataset, organize your data in YOLO format and run:

\`\`\`bash
python start.py
\`\`\`

Trained weights will be saved to `runs/detect/pen_detector/weights/best.pt`.

## Project Structure

\`\`\`
.
├── start.py          # Training script
├── webcam.py         # Real-time webcam inference
├── runs/
│   └── detect/pen_detector/weights/best.pt   # Trained model weights
└── README.md
\`\`\`

## Future Improvements

- Extend to multi-class detection (e.g., distinguishing pens vs. highlighters)
- Expand dataset size and diversity for improved accuracy
- Deploy as a web app using Streamlit or Flask

## Author

Built by Rishi as a hands-on introduction to computer vision and object detection with YOLOv8.
