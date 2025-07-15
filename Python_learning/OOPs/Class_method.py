# #step 1: Class Method Example
# class Person:
#     name = "John Doe"  # Class variable
#     age = 30  # Class variable
#     def __init__(self, name, age):
#         Person.name = name 
#         Person.age = age
        
# p1 = Person("Alice", 25)  # Instance of Person with specific name and age
# print("Name:", p1.name)
# print("Age:", p1.age) 

# print(Person.name)
# print(Person.age) 

# #step 2: Class Method Example with Class Method
# class Person:
#     name = "John Doe"  # Class variable
#     age = 30  # Class variable
    
#     # def change_name(self, new_name):
#     #     self.__class__.name = new_name # Class method to change the class variable name

#step 3: Class Method Example with Class Method
class Person:
    name = "John Doe"  # Class variable
    age = 30  # Class variable
    
    @classmethod # Class method to change the class variable
    def change_name(cls, new_name):
        cls.name = new_name  # Class method to change the class variable name
p1 = Person()  # Instance of Person
p1.change_name("Alice")  # Changing the class variable name using the class method
print("Name:", p1.name)  # Accessing the class variable name through the instance
print("Age:", p1.age)
print("Class Name:", Person.name)  # Accessing the class variable name through the class
print("Class Age:", Person.age)  # Accessing the class variable age through the class