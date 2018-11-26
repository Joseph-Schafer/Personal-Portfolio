import random
NUM_OF_RESPONSES = 3
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
lizard = "Lizard"
spock = "Spock"
cheat = "Cheat"
moves = [rock, paper, scissors,lizard,spock]
moves2 = [rock, paper, scissors,lizard,spock, cheat]
winmoves = {rock:[scissors,lizard],
            paper:[rock,spock],
            scissors:[paper,lizard],
            lizard:[paper, spock],
            spock:[scissors, rock],
            cheat: moves}


def findwinner(playermove, computermove):
    if playermove == computermove:
        
        return "Draw!"
    if computermove in winmoves[playermove]:
        
        return "Player wins!"
    
    return "Computer wins!"

def main():
    user_input = input("How many rounds do you want to play? ")
    play_times = NUM_OF_RESPONSES
    
    if (user_input.isdigit() and int(user_input) < 100):
        play_times = int(user_input)
    else:
        print("Bad input: Using default of",NUM_OF_RESPONSES)
        
    while play_times > 0:
        print("Acceptable moves:",", ".join(moves))
        playermove = input("Move: ")
        while playermove not in moves2:
            print("Bad input")
            print("Acceptable moves:",", ".join(moves))
            playermove = input("Move: ")
        computermove = random.choice(moves)
        print("Computer move:",computermove)
        print(findwinner(playermove, computermove))
        print()
        play_times -= 1
        
    print("Thanks for playing")



main()