n = int(input("Enter a number to print its multiplication table: "))
sum = 0
for i in range(1, n+1):
    sum += i  # Incrementing i by 1 in each iteration
print(sum)  # Printing the multiplication table