class Student:
    def __init__(self, nmae, marks):
        self.name = nmae
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        
s1 = Student("Mohit", 95) 
s1.display() 
s2 = Student("Prince", 85)
s2.display()
s3 = Student("Smith", 90)
s3.display
s4 = Student("Piyush", 75)
s4.display() # Calling the __str__ method to get a string representation of the object
