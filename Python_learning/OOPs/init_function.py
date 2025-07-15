class Student:
    def __init__(self):
        pass
    
    def __init__(self, name, age, id_no, cgpa):
        self.name = name
        self.age = age
        self.id_no = id_no
        self.cgpa = cgpa

s1 = Student("Mohit goswami", 20, 2365, 96.65)  # Creating an instance of the Student class with specific name and age
print("Name:  ", s1.name)
print("Age:   ", s1.age)
print("ID_No: ", s1.id_no)
print("CGPA:  \n", s1.cgpa)  

s2 = Student("Prince", 22, 1234, 8.5)  # Creating another instance of the Student class with different attributes
print("Name:  ", s2.name)  # Printing the attributes of the new Student instance
print("Age:   ", s2.age)
print("ID_No: ", s2.id_no)
print("CGPA:  ", s2.cgpa)  # Printing the CGPA of

s3 = Student("Smith", 21, 5678, 9.0)  # Creating yet another instance of the Student class
print("Name:  ", s3.name)  # Printing the attributes of the third Student
print("Age:   ", s3.age)
print("ID_No: ", s3.id_no)
print("CGPA:  ", s3.cgpa)  # Printing the CGPA of the third Student instance

s4 = Student("Piyush", 19, 9101, 7.5)  # Creating a fourth instance of the Student class
print("Name:  ", s4.name)  # Printing the attributes of the fourth Student
print("Age:   ", s4.age)
print("ID_No: ", s4.id_no)
print("CGPA:  ", s4.cgpa)  # Printing the CGPA of

