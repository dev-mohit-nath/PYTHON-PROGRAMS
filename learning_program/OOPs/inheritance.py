class Animls:
    pass

class Pets(Animls):
    pass

class Dog(Pets):
    
    @staticmethod
    def bark():
        print("bow bow!")
        


d = Dog()
d.bark()
