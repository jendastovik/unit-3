import random
import matplotlib.pyplot as plt

class SalemanMap:
    def __init__(self) -> None:
        self.x = []
        self.y = []
        self.name = []
    
    def generate_data(self, names: list):
        for name in names:
            self.name.append(name)
            self.x.append(random.randint(0, 100))
            self.y.append(random.randint(0, 100))
    def get_map(self):
        for i in range(len(self.name)):
            plt.scatter(self.x[i], self.y[i], label=self.name[i], color='red')
            plt.text(self.x[i], self.y[i], self.name[i], fontsize=10, ha="left" )
        plt.ylabel("Distance (km)")
        plt.xlabel("Distance (km)")
        #plt.yticks([20, 30, 40, 50, 60, 70, 80, 90, 100])
        plt.show()

test = SalemanMap()
test.generate_data(["Kobe", "Tokyo", "Osaka", "Nagoya", "Fukuoka", "Sapporo", "Sendai", "Kumamoto", "Naha"])
test.get_map()

class Engine:
    def __init__(self, fuel_type) -> None:
        self.fuel_type = fuel_type
        self.size_in_liters = None
        self.electic_capacity = None
    def set_size(self, size):
        self.size_in_liters = size
    def set_capacity(self, capacity):
        self.electic_capacity = capacity
    def start(self):
        print("Engine started")
    def stop(self):
        print("Engine stopped")

class LicencePlate:
    def __init__(self) -> None:
        self.letter = None
        self.numbers = None
    
    def set_letter(self, letter):
        self.letter = letter
    def set_numbers(self, numbers):
        self.numbers = numbers

class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        self.engine = None
        self.licence_plate = None

    def set_engine(self, engine: Engine):
        self.engine = engine
    
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
    def set_licence_plate(self, letter: str, numbers: int):
        self.licence_plate = LicencePlate()
        self.licence_plate.set_letter(letter)
        self.licence_plate.set_numbers(numbers)


class Car(Vehicle):
    def __init__(self, brand, model, num_doors, max_passangers) -> None:
        super().__init__(brand, model)
        self.num_doors = num_doors
        self.max_passangers = max_passangers
        self.engine = None
        self.num_passangers = 0
    def add_passanger(self):
        if self.num_passangers < self.max_passangers:
            self.num_passangers += 1
            print("Passanger added")
        else:
            print("Car is full")
    def remove_passanger(self):
        if self.num_passangers > 0:
            self.num_passangers -= 1
            print("Passanger removed")
        else:
            print("Car is empty")
    
new_car = Car("Mitsubishi", "2016", 4, 5)
new_car.set_engine(Engine("electric"))
