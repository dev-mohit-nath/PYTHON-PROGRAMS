class Car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
    @staticmethod
    def accelerate():
        print("Car is accelerating")
    @staticmethod
    def brake():
        print("Car is braking")
class Toyota(Car):
    def __init__(self, barnd):
        self.brand = barnd

class Fortuner(Toyota):
    def __init__(self, model, year, color, engine_type):
            self.engine_type = engine_type
            self.model = model
            self.year = year    
            self.color = color
car1 = Fortuner("Fortuner", 2022, "Black", "Diesel")
print(Fortuner.start())  # Accessing static method from parent class
print(Fortuner.stop())   # Accessing static method from parent class
print(Fortuner.accelerate())  # Accessing static method from parent class
print(Fortuner.brake())  # Accessing static method from parent class
print("Model:", car1.model)
print("Year:", car1.year)
print("Color:", car1.color)
print("Engine Type:", car1.engine_type)
print(Fortuner())
print("Car is a Toyota Fortuner")  # Additional information about the car
