class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def display_details(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age, salary):
        super().__init__("Enginear", "IT", salary)
        self.name = name
        self.age = age
        
engg1 = Engineer("Alice", 28, 70000)
engg1.display_details()
