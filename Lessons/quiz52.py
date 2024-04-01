import math

class Wheel:
    def __init__(self, size:float):
        self.size = size

    def get_perimeter(self):
        return self.size * math.pi
    def get_km_per_rotation(self):
        return self.get_perimeter() / 1000
    
class Bicycle:
    def __init__(self, wheel:Wheel, frame:str):
        self.wheel = wheel
        self.frame = frame
    def ride(self):
        print(f"Riding the bike with a {self.frame} frame and a wheel of size {self.wheel.size:.2f} m")
    
wheel1 = Wheel(26/39.37)
bike = Bicycle(wheel1, "aluminum")

print(f"{bike.wheel.get_km_per_rotation():.8f} km per rotation")
print(f"perimeter of the wheel: {bike.wheel.get_perimeter():.8f} m")
bike.ride()
        