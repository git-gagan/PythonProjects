from random import randint
#random module is use in python to generate random numbers and provides a lot of other functions!

def Guessit(x):
    print("The Computer has generated the number. Now it's your turn to guess it.")
    randomNumber = randint(1,x)
    guess = None
    chances = 5
    while guess != randomNumber and chances > 0:
        print(f"Number of Chances {chances}")
        if chances == 1:
            print("THIS IS YOUR FINAL CHANCE.")
        chances-=1
        guess = int(input("Make your guess :- "))
        if guess > randomNumber :
            print(f"Wrong, {guess} is too high!")
        elif guess < randomNumber :
            print(f"Wrong, {guess} is too low!")
        else:
            print(f'Woohoo! You guessed the number correctly!, It\'s {randomNumber}')
    print(f"Oh No! You ran out of chances..! Nevermind.. The answer was {randomNumber}")
    print("!-----Thanks for playing:)-----!")

if __name__ ==  "__main__":
    print("Welcome to the Guessing Game\nPlease enter the number till which you want me to generate a \
random number = ",end="")
    x=int(input())
    Guessit(x)