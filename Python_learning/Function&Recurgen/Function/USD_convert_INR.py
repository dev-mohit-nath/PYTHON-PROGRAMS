
def convertor(usd):
    inr = usd * 82.73
    print("The value in INR is:", inr)
    
usd = float(input("Enter the amount in USD: "))
convertor(usd)  # Calling the convertor function to convert USD to INR