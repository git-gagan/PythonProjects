import math
import random
import time

#Parent
class Player:
    def __init__(self,letter):
        # letter is either x or o which the player represents
        self.letter = letter

    #Given the game, we want all players to get their next move
    def move(self,game):
        pass

#Children
class Human(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter+"'s turn. Input move(0-8) : ")
            '''
            We are going to check if its correct value or not by casting it to integer
            and if it's not then we consider it invalid.
            If that spot is not available, then also invalid!
            '''
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, Try Again!\n")
        return val

class Computer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #to get move for computer, use random
        square = random.choice(game.available_moves())
        return square

#Defining the game
class TicTacToe:
    def __init__(self):
        #needs a 3*3 board to play, will use a simple list to represent our board!
        self.board = [" " for _ in range(9)]
        #to keep track of winner
        self.current_winner = None

    #Printing the board
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(" | "+" | ".join(row)+" | ")

    #Static method using decorator, Not dependent on state of object and bound to class.
    @staticmethod
    def print_board_nums():
        #Assigning numbers to spaces so that we know what number corressponds to what box!
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        print("")
        for row in number_board:
            print(" | "+" | ".join(row)+" | ")
        print("")

    #logic
    def empty_squares(self):
        #method to check if there are empty squares on the board
        return " " in self.board

    def num_empty_squares(self):
        #To get number of empty squares on board
        return self.board.count(" ")

    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == " "]
        '''
        moves = []
        for i,spot in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves
        '''
    
    def make_move(self,square,letter):
        #If valid move, then make the move i.e assign letter to square
        #else return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #Winner if 3 anywhere, horizontal, vertical or diagonal
        #First check for rows!
        row_ind = square//3 #rowIndex of our current letter
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square%3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #Check for diagonals but only if square is an even number
        #Cause that's the only way to win in this case
        if square%2 == 0:
            dia1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in dia1]):
                return True
            dia2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in dia2]):
                return True

        #if all checks fail ----> No winner yet!
        return False

def play(game, x_player, o_player,print_game = True):
    #return the winner of the game or None for Tie
    if print_game:
        game.print_board_nums()
    
    letter = "X" #starting letter
    #Iterate while the game still has empty squares
    #Dont worry about winner as we will break the loop in case of winner!
    while game.empty_squares():
        #get move from appropirate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move!
        if game.make_move(square,letter):
            if print_game:
                print("Player "+letter + f' makes a move to square {square}')
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    print(letter,"Wins!")
                    return letter
    
        #after making move, let's alternate letters!
        letter = "O" if letter == 'X' else "X"

        #tiny break
        time.sleep(0.8)   #sleep() of time suspends execution for the number of seconds provided!

    if print_game:
        print("It's a tie!")

#let's play
if __name__=="__main__":
    print("\nWelcome to TicTacToe (CLI Mode)")
    token = None
    while token != "X" and token != "O":    
        token = input("Do you want to play as X or O ? ").upper()
    if token == "X":
        x_player = Human("X")
        o_player = Computer("O")
    else:
        x_player = Computer("X")
        o_player = Human("O")
    t = TicTacToe()
    Winner = play(t,x_player,o_player)
    if Winner == token:
        print("Congrats...! You won it!\n")
    else:
        print("Better Luck Next Time!\n")