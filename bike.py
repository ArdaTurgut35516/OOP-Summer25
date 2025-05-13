class Bike:
    def __init__(self, color, bike_type, bike_size):
        self.color = color
        self.bike_type = bike_type
        self.bike_size = bike_size

bike1 = Bike("red", "city", "M")
print(f"My {bike1.bike_type} bike is {bike1.color}")

bike2 = Bike("blue", "mountain", "L")
print(f"My {bike2.bike_type} bike is {bike2.color}")

