class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def showNumber(self):
        print(f"{self.real}j + {self.imag}i")
        
    def __add__(self, num2):
        realNum = self.real + num2.real
        imagNum = self.imag + num2.imag
        return Complex(realNum, imagNum)
    def __sub__(self, num2):
        realNum = self.real - num2.real
        imagNum = self.imag - num2.imag
        return Complex(realNum, imagNum)
    def __mul__(self, num2):
        realNum = self.real * num2.real
        imagNum = self.imag * num2.imag
        return Complex(realNum, imagNum)
    def __truediv__(self, num2):
        realNum = self.real / num2.real
        imagNum = self.imag / num2.imag
        return Complex(realNum, imagNum)
    def __mod__(self, num2):
        realNum = self.real % num2.real
        imagNum = self.imag % num2.imag
        return Complex(realNum, imagNum)
    
num1 = Complex(2, 3)
num1.showNumber()  # Displaying the complex number
num2 = Complex(4, 5)
num2.showNumber()
num3 = (num1 + num2)
print(num3.showNumber())
num4 = (num1 - num2)
print(num4.showNumber())
num5 = (num1 * num2)
print(num5.showNumber())
num6 = (num1 / num2)
print(num6.showNumber())
num7 = (num1 % num2)
print(num7.showNumber())  # Displaying the result of modulus operation
