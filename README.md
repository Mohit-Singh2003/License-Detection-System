# License Plate Detection Using YOLOv5

## Project Overview
This project implements a license plate detection system using YOLOv5, compatible with both Raspberry Pi and standard PCs. The system is designed to detect and recognize license plates in real-time video feeds.

## Features
- Real-time license plate detection
- Compatible with Raspberry Pi and standard PCs
- Utilizes the YOLOv5 model for accurate detection
- Integration with Tesseract OCR for text recognition

## Requirements

### Hardware
- Raspberry Pi 3 or later / Any standard PC with a webcam

### Software
- Python 3.8+
- OpenCV
- PyTorch
- Tesseract OCR
- Ultralytics YOLOv5

## Installation
Follow the steps below to set up the project:
1. Clone the repository:
    ```bash
    git clone https://github.com/Mohit-Singh2003/License-Detection-System.git
    ```

2. Navigate to the project directory:
    ```bash
    cd License-Detection-System
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the license plate detection script, use the following command:
```bash
python app.py --source 0
