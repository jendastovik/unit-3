# Quiz 50
## Python code
```python
class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str , departure_time: str, duration: list[int]):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.duration = duration
    def get_duration(self):
        return f"{self.duration[0]} hours {self.duration[1]} minutes {self.duration[2]} seconds"

# Create two objects of the Flight class
flight1 = Flight("ABC123", "New York", "Los Angeles", "08:00", [3, 30, 0])
flight2 = Flight("DEF456", "London", "Paris", "12:30", [2, 15, 0])

# Print the duration of the first flight
print(flight1.get_duration())

# Print the duration of the second flight
print(flight2.get_duration())
```

## Output
![](/Assets/q50.png)

## UML Diagram
![](/UML/q50.png)
