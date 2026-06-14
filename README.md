# Pen Detector 🖊️

A real-time pen detection system built using **YOLOv8** and **OpenCV**. The model is fine-tuned on a custom dataset to accurately detect pens through a live webcam feed, drawing bounding boxes and confidence scores in real time.

---

## Demo

Run `webcam.py` to start live pen detection using your webcam.

### Sample Detection

> Add screenshots or a GIF here to showcase real-time detection.

```md
![Detection Demo](demo.gif)
```

---

## Project Overview

This project demonstrates a complete custom object detection pipeline, from data collection to real-time deployment.

### Workflow

1. **Data Collection**
   - Collected and curated 120+ images of pens in different orientations, lighting conditions, and backgrounds.

2. **Annotation**
   - Annotated images using Roboflow and exported them in YOLOv8 format.

3. **Training**
   - Fine-tuned a pretrained YOLOv8n model on the custom dataset.

4. **Inference**
   - Developed a real-time detection application using OpenCV and webcam input.

---

## Model Details

| Property | Value |
|----------|---------|
| Model | YOLOv8n (Nano) |
| Task | Single-Class Object Detection |
| Framework | Ultralytics YOLOv8 |
| Backend | PyTorch |
| Training Epochs | 80 |

---

## Results

The model was trained for 80 epochs and evaluated on a validation dataset.

| Metric | Score |
|----------|---------|
| Precision | 0.960 |
| Recall | 0.851 |
| mAP@50 | 0.926 |
| mAP@50-95 | 0.522 |

### Training Visualizations

> Add YOLO-generated evaluation plots for better project presentation.

```md
![Results](results.png)
![Confusion Matrix](confusion_matrix.png)
```

---

## Tech Stack

- **YOLOv8 (Ultralytics)** – Object Detection
- **OpenCV** – Webcam Capture & Visualization
- **PyTorch** – Deep Learning Framework
- **Roboflow** – Data Annotation & Preprocessing

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd pen-detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install ultralytics opencv-python
```

---

## Usage

### Real-Time Detection

```bash
python webcam.py
```

A webcam window will open and display detected pens with bounding boxes and confidence scores.

Press **q** to exit.

### Retrain the Model

```bash
python start.py
```

The best-performing model weights will be automatically saved in the YOLO training output directory.

---

## Project Structure

```text
.
├── start.py
├── webcam.py
├── requirements.txt
├── README.md
├── dataset/
├── runs/
│   └── detect/
│       └── ...
└── assets/
    ├── demo.gif
    ├── results.png
    └── confusion_matrix.png
```

---

## Future Improvements

- Increase dataset size for improved generalization
- Support multiple stationery classes (pens, pencils, markers, highlighters)
- Improve performance in challenging lighting conditions
- Deploy as a web application using Streamlit or Flask
- Export the model to ONNX/TensorRT for optimized inference

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Data collection and annotation
- Custom object detection model training
- YOLOv8 workflow and deployment
- Real-time computer vision applications
- OpenCV integration with deep learning models

---

## License

This project is licensed under the MIT License.

---

## Author

**Rishi Bansal**

A hands-on computer vision project exploring custom object detection using YOLOv8, covering the complete pipeline from dataset creation and annotation to training and real-time deployment.