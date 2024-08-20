import random

def user_choice():
    while True:
        rps_choice = input("Choose rock, paper, or scissors: ").lower()
        if rps_choice in ["rock", "paper", "scissors"]:
            return rps_choice
        else:
            print("Invalid choice, try again!")

def comp_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner_select(user, comp):
    if user == comp:
        return None
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        return "user"
    else:
        return "computer"

def game_play(rounds, points_to_win):
    user_points = 0
    comp_points = 0

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")
        user = user_choice()
        comp = comp_choice()
        print(f"Computer chose: {comp}")
    
        winner = winner_select(user, comp)
        if winner == "user":
            user_points += 1
            print("You win this round!")
        elif winner == "computer":
            comp_points += 1
            print("The computer wins this round!")
        else:
            print("This round is a tie!")
        
        print(f"Score: You {user_points} - {comp_points} Computer")
    
        if user_points == points_to_win:
            print("Congratulations! You win the game!")
            return
        elif comp_points == points_to_win:
            print("Sorry, the computer wins the game.")
            return

    # Final result if no early termination
    if user_points > comp_points:
        print("You win the game!")
    elif comp_points > user_points:
        print("The computer wins the game.")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    rounds = 3
    points_to_win = 2
    game_play(rounds, points_to_win)
