import random

def rules():
    print("Here we go, ALL THE BEST!")
    rounds=1
    user_score=0
    comp_score=0
    while rounds<4:
        print(f"Round {rounds}")
        user=input("What's your choice?\nEnter p for Paper, r for Rock, s for Scissors :- ").lower()
        if user!="r" and user!="s" and user!="p":
            return "Invalid Input given! You are thrown out of the game, TRY AGAIN LATER!"
        computer=random.choice(["r","p","s"])
        #returns a random element from a specified sequence
        if user==computer:
            print("Tie, No score given\n")
        
        elif win(user,computer):
            print("You won this round\n")
            user_score+=1
        else:
            print("You lose this round\n")
            comp_score+=1

        rounds+=1
    print("Game Over! Here are the results :")

    if user_score>comp_score:
        return f"You won! Your Score={user_score}"
    elif user_score<comp_score:
        return f"You lost! Your Score={user_score}"
    else:
        return "It's a tie!"

def win(player, opponent):
    if (player=="s" and opponent=="p") or (player=="r" and opponent=="s") or (player=="p" and opponent=="r"):
        return True

if __name__=="__main__":
    print("-----Welcome to the Rock, Paper, Scissors Game-----\nYou will be playing against the Computer!")
    name=input("Please enter your name :- ")
    print(rules())
    print("Thanks for Playing!\n")