import cv2
import pytesseract
import pandas as pd
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

car_database = pd.read_csv('new.csv')  # Replace 'new.csv' with the actual file name

image = cv2.imread('123456.png')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


custom_config = r'--oem 3 --psm 6'
number_plate_text = pytesseract.image_to_string(gray, config=custom_config)

print("Extracted Number Plate:", number_plate_text)

number_plate_text = re.sub(r'\W+', '', number_plate_text.upper())

# Convert the extracted number plate text to an integer
extracted_number_plate = int(number_plate_text)

matching_car = car_database[car_database['Number Plate'] == extracted_number_plate]

if not matching_car.empty:
    print("Matching Car Details:")
    for column_name, detail in matching_car.iloc[0].items():
        print(f"{column_name}: {detail}")
else:
    print("No matching car found in the database.")
