def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)# Printing the factorial at each step
    
n = int(input("Enter a number to calculate its factorial: "))
result = fact(n)
print(f"The factorial of {n} is: {result}")  # Printing the final result