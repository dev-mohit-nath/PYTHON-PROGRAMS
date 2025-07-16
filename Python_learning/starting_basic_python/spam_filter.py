p1 = "Make a lot of money"
p2 = "Buy now and get rich quick"
p3 = "Limited time offer"
p4 = "Congratulations, you've won a lottery"
p5 = "Free access to exclusive content"

masage = input("Enter your commant: ")

if(p1 in masage or p2 in masage or p3 in masage or p4 in masage or p5 in masage):
    print("This is a spam message")
else:
    print("This is not a spam message")