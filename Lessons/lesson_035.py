class Car:
    def __init__(car, brand, model, year):
        car.brand = brand
        car.model = model
        car.year = year
        car.kilometers = 0

    def __str__(car):
        return f"car with specs: {car.brand} {car.model} {car.year}"
    def get_model(car):
        return car.model
    def set_year(car, year):
        car.year = year
    def get_state(car):
        ans = ""
        if car.year > 2021 and car.kilometers < 1000:
            ans = "new"
        elif car.year > 2018 and car.kilometers < 100000:
            ans = "good"
        else:
            ans = "bad"
        return ans
        

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)
print(my_car)
print(my_car.get_model())
print(Car.get_model(my_car))

# Change the year of the car
my_car.set_year(2023)
print(my_car)
