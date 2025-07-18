class Student:
    def __init__(self,name):
        self.name = name
        
s1 = Student("Mohit")
print("Name:", s1.name)
del s1.name  # Using the del keyword to delete the instance s1
print(s1.name) # This will raise an error since s1 has been deleted