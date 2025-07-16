import random

guess_the_number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter random number(y/n): "))
        if(guess < guess_the_number):
            print("Too high")
        elif(guess > guess_the_number):
            print("Too low:")
        else:
            print("congratulation! you guessed the number")
    except:
        print("pleace enter the valid number")

