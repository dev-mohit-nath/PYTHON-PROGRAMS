class Student:
    def __init__(self, py, math, eng, hist, geo):
        self.py = py
        self.math = math
        self.eng = eng
        self.hist = hist
        self.geo = geo
        
    @property
    def percentage(self):
        return (self.py + self.math + self.eng + self.hist + self.geo) / 5
        # step 1:
    # def percentage(self):
    #     total_marks = self.py + self.math + self.eng + self.hist + self.geo
    #     return total_marks / 5
        
    def display(self):
        print("Physics: ", self.py)
        print("Maths:   ", self.math)
        print("English: ", self.eng)
        print("History: ", self.hist)
        print("Geography:", self.geo)
        print("Percentage: ", self.percentage, "%")
        
s1 = Student(85, 90, 88, 92, 87)
s1.py = 100
s1.math = 95
s1.display()  # Displaying the marks and percentage of the student