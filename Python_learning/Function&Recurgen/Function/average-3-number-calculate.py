def calcAvg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print("The average is:", avg) 
    return avg

nym1 = float(input("Enter First number: "))
nym2 = float(input("Enter Second number: "))
nym3 = float(input("Enter Third number: "))
avg = calcAvg(nym1, nym2, nym3)