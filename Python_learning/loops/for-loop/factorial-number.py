n = int(input("Enter a factorial number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)  # Printing the factorial of n