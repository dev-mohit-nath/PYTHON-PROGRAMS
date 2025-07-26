def main():
    try:
        a = int(input("Enter a number:"))
        print(a)
    except ValueError as e:
        print(e)
        
    finally:
        print("this is a program run sucesfully.")
        
main()