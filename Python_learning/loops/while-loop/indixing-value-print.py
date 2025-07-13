
list = [1, 4, 6, 9, 10, 13, 25, 45, 67, 89, 90, 100] 
i = 0
while i < len(list):
    print (list[i])
    i += 1 # Incrementing i by 1 in each iteration
    

num = (1, 4, 6, 9, 10, 13, 25, 30, 45, 67, 83, 90, 90, 100)
x = int(input("Enter a value to find its index: "))
i = 0
while i < len(num):
    if num[i] == x:
        print("value is founded at index:", i)
    else:
        print("Lodding...")
    i += 1  # Incrementing i by 1 in each iteration