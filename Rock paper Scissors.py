import random

def play():
    user = input("(R) for Rock, (P) for Paper, (S) for Scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    # determining the different outcomes after computer and player choose a move
    if user == computer:
        return f"It's a tie! You both chose {written(computer)}"
    if wincondition(user,computer):
        return f"You won! The computer chose {written(computer)}"
    
    return f"You lost! The computer chose {written(computer)}"

def wincondition(player, opponent):
    # rock > scissors, scissors > paper, paper > rock
    if (player == 'r' and opponent == 's') or {player == 's' and opponent == 'p'} or {player == 'p' and opponent == 'r'}:
        return True

def playagain():
    # choose to play again after a round of rock paper scissors
    playagain = input("Do you want to play again? (y/n): ")
    if playagain == "y":
        main()
    else:
        pass
        
# returns the choice of player after winner is determined
def written(choice):
    match choice:
        case "r":
            return "Rock"
        case "p":
            return "Paper"
        case "s":
            return "Scissors"
        case _:
            return "Invalid input"
    

def main():
    print("Let's play Rock Paper Scissors! Choose your move:")
    print(play())
    playagain()
    
main()
print("Thanks for playing!")
