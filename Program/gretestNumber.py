a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

if(a >= b and a >= c):
    print(f"First number is largest:",a)
elif(b >= c):
    print(f"Second number is largest",b)
else:
    print(f"Third number is largest",c) 