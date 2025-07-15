import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess a Target and quit(Q): ")
    if (userChoice == 'Q'):
        break
    
    userChoice = int(userChoice)
    if userChoice == target:
        print("Your guess is too low. Try again.")
        break
    elif userChoice < target:
        print("Your guess is too high. Try again.")
    else:
        print("Congratulations! You've guessed the number correctly.")
        
print("<-----Game Over!------>")  # Indicating the end of the game