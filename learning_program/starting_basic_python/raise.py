a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(f"The value of Devisible Value {a/b}.")

if(b==0):
    raise ZeroDivisionError("Can't divide by zero.")
else:
    print(f"The division a/b is {a/b}")
    
print("this is a program by run4")