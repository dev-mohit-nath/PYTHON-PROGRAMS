class Student:
    def __init__(self,full_name="Mohit goswami", age=20, id_no=101, cgpa=9.5): 
        self.name = "Mohit goswami"
        self.age = 20
        self.id_no = 101
        self.cgpa = 9.5
    
s1 = Student()  # Creating an instance of the Student class
print("Name:  ",s1.name) 
print("Age:   ",s1.age) 
print("ID_No: ",s1.id_no)
print("CGPA:  ",s1.cgpa)  # Printing the attributes of the Student instance  
