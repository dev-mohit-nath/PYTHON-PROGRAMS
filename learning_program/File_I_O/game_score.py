import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 80)
    
    with open("C:\python\Python_learning\File_I_O\hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
        print(f"Yore Score: {score}") 
        
        if score>hiscore:
            with open("C:\python\Python_learning\File_I_O\hiscore.txt", "w") as f:
                f.write(str(score))
        
        return score          
    
game()