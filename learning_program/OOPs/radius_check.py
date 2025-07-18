class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)  # Creating an instance of Circle with radius 5
print("Area of Circle:", c1.area())  # Displaying the area of the circle
print("Perimeter of Circle:", c1.perimeter())  # Displaying the perimeter of the circle
