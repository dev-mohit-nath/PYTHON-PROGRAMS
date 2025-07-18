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

class ElectricCar(Car):
    def __init__(self, battery_capacity, speed, color):
        self.battery_capacity = battery_capacity
        self.speed = speed
        self.color = color

car1 = ElectricCar(75 , 120, "blue")

print(ElectricCar.start())  # Accessing static method from parent class
print(ElectricCar.stop())   # Accessing static method from parent class
print(ElectricCar.accelerate())  # Accessing static method from parent class
print("Battery Capacity:", car1.battery_capacity, "kWh")
print("Speed:", car1.speed, "km/h")