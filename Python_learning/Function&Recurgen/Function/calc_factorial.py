def calc_fact(n):
    fact = 1
    for i in range(1, n +1):
        fact *= i
    print(fact)

n = int(input("Enter a number to calculate its factorial: "))
result = calc_fact(n)