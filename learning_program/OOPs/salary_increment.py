class Employee:
    salary = 230
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100 
        
        
em1 = Employee()
em1.salaryAfterIncrement = 280
print(em1.increment)