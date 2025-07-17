def calulater():
    while True:
        num1 = input("Enter first number: ")
        op = input("Enter a operator(+,-,*,/):")
        num2 = input("Enter second number: ")
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid number! please enter numeric Value.")
            continue

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid operator! use (+,-,*,/)")
            continue
        print(f"Result: {num1} {op} {num2} = {result}")
        
        
        again = input("Do yo want to calculate again? (y/n):").lower()
        
        if again != 'y':
            print("Thank you for using the calculate!")
            break
        
calulater()
            
        
    


