import cv2
import pytesseract
from ultralytics import YOLO

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

model = YOLO(r"C:\Users\mksin\OneDrive\Desktop\YOLO\dataset\best.pt")

# Update with the correct MJPEG stream URL
ip_camera_url = "http://192.168.1.22:8080/video"  # Replace with actual video stream URL
cap = cv2.VideoCapture(ip_camera_url)

with open("license_plates.txt", "w") as file:
    recognized_plates = set()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, show=True)

        for result in results:
            for detection in result.boxes:
                if detection.conf >= 0.88:
                    x1, y1, x2, y2 = map(int, detection.xyxy[0])

                    license_plate_img = frame[y1:y2, x1:x2]

                    license_plate_text = pytesseract.image_to_string(
                        license_plate_img, config="--psm 8"
                    ).strip()

                    if (
                        license_plate_text
                        and license_plate_text not in recognized_plates
                    ):
                        recognized_plates.add(license_plate_text)
                        file.write(f"{license_plate_text}\n")

cap.release()
print("License plate numbers saved to license_plates.txt.")
