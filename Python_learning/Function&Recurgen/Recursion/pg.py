def greatestNumber(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 3
b = 4
c = 9

print(greatestNumber(a, b, c))
    