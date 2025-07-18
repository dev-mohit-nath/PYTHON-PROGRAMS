list = (1, 4, 9, 16, 20, 60, 45, 60, 75, 86, 98, 100)
x = int(input("Enter a value to find its index: "))
idx = 0
for el in list:
    if el == x:
        print("value is found at index:", idx)
    idx += 1  # Incrementing idx by 1 in each iteration