from datetime import datetime, timedelta

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.entry_time = None
        self.exit_time = None

    def enter_parking_lot(self):
        self.entry_time = datetime.now()
        print(f"Car with license plate {self.license_plate} entered the parking lot at {self.entry_time}")

    def exit_parking_lot(self):
        if self.entry_time is not None:
            self.exit_time = datetime.now()
            duration = self.exit_time - self.entry_time
            print(f"Car with license plate {self.license_plate} exited the parking lot at {self.exit_time}")
            print(f"Total parking duration: {duration}")

def main():
    # Create cars
    car1 = Car("KBX 4032S")
    car2 = Car("KDD 8269T")

    # Simulate car entry
    car1.enter_parking_lot()
    car2.enter_parking_lot()

    # Simulate car exit
    car1.exit_parking_lot()
    car2.exit_parking_lot()

if __name__ == "__main__":
    main()
