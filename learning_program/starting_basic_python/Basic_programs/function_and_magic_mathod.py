# Define a function
def greet(name):
    print("Hello, " + name + "!")

# Call the function
greet("John")

# Define a class with magic methods
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hello, my name is " + self.name + "!"

# Create an instance of the class
person = Person("John")
print(person)
