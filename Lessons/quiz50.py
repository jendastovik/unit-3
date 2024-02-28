class Aircraft:
    def __init__(self, model:str, capacity:int):
        self.model = model
        self.capacity = capacity

    def get_info(self):
        return f"{self.model} (Capacity: {self.capacity})"

class Flight(Aircraft):
    def __init__(self, flight_number: str, origin: str, destination: str , departure_time: str, duration: list[int], model:str, capacity:int):
        super().__init__(model, capacity)
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration
    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes {self.duration[2]} seconds"\
        
    def get_info(self):
        return f"FLight {self.flight_number} from {self.origin} to {self.destination} departs at {self.departure_time}. {super().get_info()}"

def print_object_info(obj):
    print(obj.get_info())

# Create two objects of the Aircraft class
aircraft1 = Aircraft("Boeing 747", 366)
aircraft2 = Aircraft("Airbus A380", 509)

# Create two objects of the Flight class
flight1 = Flight("ABC123", "New York", "Los Angeles", "08:00", [3, 30, 0], "Boeing 747", 366)
flight2 = Flight("DEF456", "London", "Paris", "12:30", [2, 15, 0], "Airbus A380", 509)

# Print the duration of the first flight
print(flight1.get_duration())

# Print the duration of the second flight
print(flight2.get_duration())

# Print the information
print_object_info(flight1)
print_object_info(aircraft1)





