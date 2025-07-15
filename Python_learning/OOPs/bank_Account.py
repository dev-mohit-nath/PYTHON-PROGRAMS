class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def deposit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited from your account.")
        print("Total balance is:", self.total_balance()) 
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited to your account.")  
        print("Total balance is:", self.total_balance())    
    
    def total_balance(self):
        return self.balance  

acc1 = Account(10000, 58496) 
acc1.deposit(5000)  # Depositing an amount into the account
acc1.credit(2000)   # Crediting an amount to the account