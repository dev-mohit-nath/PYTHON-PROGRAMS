class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
    
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        super().stop()
car1 = ToyotaCar("prius", "Electric")
print(car1.name)
print(car1.type)
        