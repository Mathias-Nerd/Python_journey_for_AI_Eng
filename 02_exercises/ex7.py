#Rock, Paper, Scissors Game
def rock_paper_scissors():
    Player1 = input("PLayer1: Enter your value: ").lower()
    Player2 = input("PLayer2: Enter your value: ").lower()
    if Player1 == Player2:
        print("The game is a tie")
    elif Player1 == "rock":
        if Player2 == "scissors":
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif Player1 == "scissors":
        if Player2 == "paper":
            print("Player1 wins")
        else:
            print("Player2 wins")
    elif Player1 == "paper":
        if Player2 == "scissors":
            print("Player1 wins")
        else:
            print("Player2 wins")
    else:
        print("Wrong input")
    
    print("Would you like to play again? Enter yes or no")
    if input().lower == "yes":
        rock_paper_scissors()
    else:
        print("Game ended")

rock_paper_scissors()