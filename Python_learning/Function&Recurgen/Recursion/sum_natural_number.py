def sum_natural_numbers(n):
    if n == 0: # Base case: if n is 0, return 0
        return 0
    else:
        return n + sum_natural_numbers(n - 1)  # Recursive call to sum the numbers
    
n = int(input("Enter a natural number: "))
print(f"The sum of natural numbers up to {n} is: {sum_natural_numbers(n)}")  # Printing the sum