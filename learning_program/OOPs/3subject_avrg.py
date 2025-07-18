class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def get_avrg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Name:", self.name, "\nAverage:", sum /3)

s1 = Student("Mohit Goswami", [90, 69, 88]) 
s1.get_avrg()

s2 = Student("Prince", [85, 75, 95])
s2.get_avrg()

s3 = Student("Smith", [80, 90, 70])
s3.get_avrg()

