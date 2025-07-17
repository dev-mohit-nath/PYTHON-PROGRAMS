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

    elif (you == -1 and computer == 1) or \
         (you == 1 and computer == 0) or \
         (you == 0 and computer == -1):
        print("You win!")
    else:
        print("You lose!")
