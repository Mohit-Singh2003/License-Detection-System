<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>License Plate Detection Using YOLOv5</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>License Plate Detection Using YOLOv5</h1>

    <h2>Project Overview</h2>
    <p>This project implements a license plate detection system using YOLOv5, compatible with both Raspberry Pi and standard PCs. The system is designed to detect and recognize license plates in real-time video feeds.</p>

    <h2>Features</h2>
    <ul>
        <li>Real-time license plate detection</li>
        <li>Compatible with Raspberry Pi and standard PCs</li>
        <li>Utilizes the YOLOv5 model for accurate detection</li>
        <li>Integration with Tesseract OCR for text recognition</li>
    </ul>

    <h2>Requirements</h2>
    <h3>Hardware</h3>
    <ul>
        <li>Raspberry Pi 3 or later / Any standard PC with a webcam</li>
    </ul>

    <h3>Software</h3>
    <ul>
        <li>Python 3.8+</li>
        <li>OpenCV</li>
        <li>PyTorch</li>
        <li>Tesseract OCR</li>
        <li>Ultralytics YOLOv5</li>
    </ul>

    <h2>Installation</h2>
    <p>Follow the steps below to set up the project:</p>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/Mohit-Singh2003/License-Detection-System.git</code></pre>
        
        <li>Navigate to the project directory:</li>
        <pre><code>cd License-Detection-System</code></pre>

        <li>Install the required packages:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

    <h2>Usage</h2>
    <p>To run the license plate detection script, use the following command:</p>
    <pre><code>python app.py --source 0</code></pre>
    <p>Replace <code>0</code> with the path to your video file or the URL of your IP camera stream if you wish to use a live feed.</p>

    <h2>Contributing</h2>
    <p>Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>

    <h2>Contact</h2>
    <p>For any inquiries, please contact:</p>
    <p>Mohit - <a href="mailto:mohitucsss@gmail.com">mohitucsss@gmail.com</a></p>

</body>
</html>
