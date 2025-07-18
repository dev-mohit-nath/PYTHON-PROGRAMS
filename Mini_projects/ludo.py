import random
import time

players ={
    "Red" : 0,
    "Blue" : 0,
    "Green" : 0,
    "Yellow" : 0
}

WINNING_POSITION = 100
finished_players = []

def roll_dice():
    return random.randint(1, 6)

def show_leaderboard():
    leaderboard = sorted(players.items(), key = lambda x: x[1], reverse =True)
    print("\n🥇 Leaderboard:")
    for p, score in leaderboard:
        print(f"{p}: {score}")
    print("-" * 30)
    
def show_position():
    print("\n📊 Current positions:")
    for p, pos in players.items():
        print(f"{p}: {pos}")
    print(f"-" * 30)
    
def play_ludo():
    print("🎲 Ludo game start! first to reach 100 wins.")
    print("Rules: 🎯Role a 6 to go again | :💥land on opponent = send to 0\n")
    
    while len(finished_players) < 4:
        for player in players:
            if player in finished_players:
                continue
            
            input(f"{player}'s turn. Press Enter to roll the dice...")
            
            while True:
                print("Rolling", end ="")
                for _ in range(3):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                print()
                
                dice = roll_dice()
                print(f"{player} rolled a {dice}")
                
                if players[player] + dice <= WINNING_POSITION:
                    players[player] += dice
                    print(f"{player} move to {players[player]}")
                else:
                    print(f"{player} needs exectly {WINNING_POSITION - players[player]} to win.")
                    
                    
                for opponent in players:
                    if opponent != player and players[opponent] == players[player] and players[player] != 0:
                        print(f"💥 {player} landed on {opponent}! {opponent}goes back to 0.")
                        players[opponent] = 0
                        
                if players[player] == WINNING_POSITION and player not in finished_players:
                    print(f"🏴 {player} has reached the goal!")
                    finished_players.append(player)
                    break
                
                if dice != 6:
                    break
                else:
                    print(f"{player} rolled a 6! Roll again.\n")
                    
            show_position()
            show_leaderboard()
    #Game over
    print(f"\n🎉 All player finished!")
    print("🏆Final Rankings:")
    for i, p in enumerate(finished_players, start=1):
        print(f"{i}. {p}")

#Start the game
if __name__ == "__main__":
    play_ludo() 
            
                
                    
