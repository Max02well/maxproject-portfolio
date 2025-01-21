import datetime

class Car:
    def __init__(self, plate_number, entry_time):
        self.plate_number = plate_number
        self.entry_time = entry_time
        self.exit_time = None

    def park(self):
        self.entry_time = datetime.datetime.now()

    def leave(self):
        self.exit_time = datetime.datetime.now()

    def get_duration(self):
        if self.exit_time is not None:
            duration = self.exit_time - self.entry_time
            return duration
        else:
            return datetime.datetime.now() - self.entry_time

def main():
    parking_lot = []

    while True:
        print("\n1. Park a car")
        print("2. Leave the parking lot")
        print("3. Display parked cars and durations")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            plate_number = input("Enter car plate number: ")
            car = Car(plate_number, datetime.datetime.now())
            parking_lot.append(car)
            print(f"Car {plate_number} parked at {car.entry_time}")

        elif choice == '2':
            plate_number = input("Enter car plate number to leave: ")
            for car in parking_lot:
                if car.plate_number == plate_number:
                    car.leave()
                    duration = car.get_duration()
                    print(f"Car {car.plate_number} left. Parking duration: {duration}")
                    parking_lot.remove(car)
                    break
            else:
                print(f"Car with plate number {plate_number} not found in the parking lot.")

        elif choice == '3':
            print("\nCars parked and their durations:")
            for car in parking_lot:
                duration = car.get_duration()
                print(f"Car {car.plate_number}: {duration}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

#This code defines a `Car` class with methods for parking, leaving, and calculating the duration of parking. The `main` function acts as the user interface to park and leave cars, display parked cars, and exit the program. The parking durations are calculated using the `datetime` module.