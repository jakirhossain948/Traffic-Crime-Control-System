import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_frame(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morphed = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

    return morphed

video_capture = cv2.VideoCapture('video.mp4')  # Replace 'car_video.mp4' with the actual video file name

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    processed_frame = preprocess_frame(frame)

    custom_config = r'--oem 3 --psm 6'
    number_plate_text = pytesseract.image_to_string(processed_frame, config=custom_config)

    print("Extracted Number Plate:", number_plate_text)

    number_plate_text = re.sub(r'\W+', '', number_plate_text.upper())

    cv2.putText(frame, number_plate_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
