import csv
from faker import Faker

fake = Faker()

def generate_car_data():
    number_plate = fake.random_int(min=100, max=999) * 1000 + fake.random_int(min=10, max=99)
    registration_number = fake.random_int(min=10000, max=99999)
    make = fake.random_element(elements=('Toyota', 'Honda', 'Ford', 'Chevrolet', 'Hyundai'))
    model = fake.random_element(elements=('Corolla', 'Civic', 'Fusion', 'Cruze', 'Elantra'))
    model_year = fake.random_int(min=2010, max=2023)
    body_style = fake.random_element(elements=('Sedan', 'SUV', 'Truck', 'Hatchback', 'Coupe'))
    color = fake.color_name()
    engine = fake.random_element(elements=('2.0L Inline-4', '1.5L Turbocharged Inline-4', '3.6L V6', '2.4L Inline-4', '1.6L Turbocharged Inline-4'))
    transmission = fake.random_element(elements=('Automatic', 'Manual', 'CVT'))
    drivetrain = fake.random_element(elements=('Front-Wheel Drive', 'Rear-Wheel Drive', 'All-Wheel Drive'))
    fuel_economy = f"{fake.random_int(min=20, max=40)} mpg"
    features = ', '.join(fake.words(nb=3, ext_word_list=None, unique=True))
    safety_ratings = fake.random_element(elements=('5-star', '4-star', '3-star'))
    mileage = fake.random_int(min=1000, max=100000)
    service_history = fake.random_element(elements=('Regularly serviced', 'Service records available', 'No service history'))
    price = f"${fake.random_int(min=1000, max=50000)}"
    location = fake.city()

    return [number_plate, registration_number, make, model, model_year, body_style, color, engine, transmission, drivetrain, fuel_economy, features, safety_ratings, mileage, service_history, price, location]

def generate_car_data_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Number Plate", "Registration Number", "Make", "Model", "Model Year", "Body Style", "Color", "Engine", "Transmission", "Drivetrain", "Fuel Economy", "Features", "Safety Ratings", "Mileage", "Service History", "Price", "Location"])
        for _ in range(num_rows):
            writer.writerow(generate_car_data())

if __name__ == "__main__":
    generate_car_data_csv("car_data_100000.csv", 100000)
   