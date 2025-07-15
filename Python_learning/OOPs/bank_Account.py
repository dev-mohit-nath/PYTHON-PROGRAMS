class Account:
    def _init(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def deposit(self, amount):
        self.blance -= amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
        print("Total balance is:", self.total_balance()) 
    
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}.")  
        print("Total balance is:", self.total_balance())    
    
    def total_balance(self):
        return self.balance  

acc1 = Account(1000, 123456) 
print(acc1.blance) # Credit amount to the account
print(acc1.acc_no) # Credit amount to the account