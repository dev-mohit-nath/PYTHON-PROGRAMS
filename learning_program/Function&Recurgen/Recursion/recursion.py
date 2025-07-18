def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)  # Recursive call to show the next number down to 0
    
n = int(input("Enter a number to show in reverse order: "))
show(n)  # Calling the show function to print numbers in reverse order from n to