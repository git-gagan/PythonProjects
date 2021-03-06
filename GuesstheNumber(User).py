from random import randint

def comp_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!="c":
        if low!=high:
            c_guess=randint(low,high)
        else:
            c_guess=low #Can also be high since low=high
        feedback=input(f"Is {c_guess} high(H), low(L) or correct(C)? ").lower()
        if feedback=="l":
            low=c_guess+1
        elif feedback=="h":
            high=c_guess-1
        else:
            print("Yay, You guessed it correctly, The answer is",Number)
    print("Thanks for playing!")


if __name__=="__main__":
    print("Welcome to the guessing game. Please enter your name here..")
    name=input()
    print("Please Input a random Number you want the Computer to guess later on :- ",end="")
    Number=int(input())
    print("Enter the range upto which the computer shall explore :- ",end="")
    x=int(input())
    comp_guess(x)