Automatic Car Number Plate Recognition System

This project is designed to perform Automatic Number Plate Recognition using Python, OpenCV, and Tesseract.

It includes two main components:
1. Main Module: This module extracts the number plate from an input image and video that performs optical character recognition (OCR) using Tesseract and matches the extracted number plate with entries in a car database to provide details of the corresponding vehicle.

2.Demo Dataset Constraction: This module generates synthetic car data and exports it to a CSV file, which can be used as the car database for the ANPR module.

Ensure you have the following installed:

- Python (version 3.x)
- OpenCV (cv2)
- Tesseract OCR
- pytesseract
- pandas
- faker

You can install dependencies using pip:

pip install opencv-python pytesseract pandas faker
python anpr.py
python generate_car_data.py

