class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n * self.n}")
    def cube(self):
        print(f"The square is {self.n * self.n * self.n}")
    def squareRoot(self):
        print(f"The square is {self.n**1/2}")
        
        
c1 = Calculator(4)

c1.square()
c1.cube()
c1.squareRoot()