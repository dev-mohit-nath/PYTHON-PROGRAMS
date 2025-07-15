class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no # Public attribute
        self.__acc_pass = acc_pass # Private attribute
    def reset_pass(self): # Method to access the private attribute
        print(self.__acc_pass)
    
    def __User(self): # Private method
        print("This is a private method.")
    def get_user(self): # Public method to access the private method
        self.__User()

s1 = Account(123456, "password123")
print("Account Number:", s1.acc_no)
print(s1.reset_pass()) # Accessing the private method to print the password
print(s1.get_user()) # Accessing the private method to print the user information
#print("Account Password:", s1.__acc_pass) # This will raise an error since __acc_pass is private and cannot be accessed directly