try:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")