import random
def diceRole():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice Rolled: {dice1}, {dice2}")
    print(f"Total Dice: {dice1 + dice2} ")
while True:
    choice = input("Role the dice? (y/n):").lower()
    if choice == 'y':
        diceRole()
    elif choice == 'n':
        print("Exit the game")
        break
    else:
        print("Envlaid choice")