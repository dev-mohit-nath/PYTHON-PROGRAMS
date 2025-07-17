import random
'''
snake = -1
water = 1
gun  = 0

'''
youstr = input("Enter your choice: ").lower()

youDict = {"s": -1, "w": 1, "g": 0}
reversedDict = {-1: "snake", 1: "water", 0: "gun"}

computer = random.choice([-1, 0, 1])


if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")

    if(computer == you):
        print("Game is draw.")

    else:
        if(computer == -1 and you == 1):
            print("you win!")
        elif(computer == 1 and you == -1):
            print("you lose!")
        elif(computer == 1 and you == 0):
            print("you win!")
        elif(computer == 0 and you == 1):
            print("you lose!")
        elif(computer == -1 and you == 0):
            print("you lose!")
        elif(computer == 0 and you == -1):
            print("you win!")
    
