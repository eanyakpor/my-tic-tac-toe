import random
'''
TicTacToe - Emi Anyakpor Jr. 9/8/24 

2 players Computer vs the User
in a 3 x 3 grid a player wins by getting 3 O in a row or column
or 3 X in a row or column 
utilize object oriented programming to complete this game in python

create win method?
Create player methods 
Create random function for Computer to chose on each round 
round will not end until someone wins, someone will always win or end in a draw 

'''

class TicTacToe: 
    # only player1 will choose there name and marker 
    def __init__(self, player1_name,player1_marker):
        self.player1 = HumanPlayer(player1_name,player1_marker)
        player2_marker = 'O' if player1_marker == 'X' else 'X'
        self.player2 = ComputerPlayer("Bot", player2_marker)
        print(f'{self.player1}, is you and {self.player2}, is the computer')    
        self.board = [['Nan' for _ in range(3)] for _ in range(3)]
        self.current_player = self.player1

    # prints the board in the game 
    def printBoard(self):
        for r in range(len(self.board)):
            # print statements create new line by defualt which is why we need all sperator printed out at once 
            print('-' * (len(self.board) * 8))
            for c in range(len(self.board)):
                # prints without adding new line for each column 
                print(f'| {self.board[r][c]} |', end = ' ')
            print('\n')
            
        print('-' * (len(self.board)* 8 ))

    # current palyer gets switched off since this is a turn based game 
    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
            
    def is_board_full(self):
        return 'NaN' not in self.board

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != 'NaN':
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != 'NaN':
                return True
    
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 'NaN':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 'NaN':
            return True
        
        return False
                
    def play_game(self):
        print('hello')
        while True:
            self.printBoard()
            # allowing each player to make a move 
            self.current_player.make_move(self.board)
            # consintely checks for a winner of the current player
            if self.check_winner():
                self.printBoard()
                print(f"{self.current_player.name} wins!")
                break
            # if the board is full then that means it's a tie 
            if self.is_board_full():
                self.printBoard()
                print("It's a tie!")
                break 
            
            # After every turn switch the player 
            self.switch_player()
                
class Player:

    # player class and has a make_move functions 
    # will be one for computer : player2 
    # one for user : player1
    def __init__(self, name, marker):
        self.name = name 
        self.marker = marker

# have to do this since python prints the memory address of objects by default 
# Override the __str__ method
    def __str__(self):
        return f"{self.name} ({self.marker})"

    def make_move(self,board):
        raise NotImplementedError("This method should be overriden by subclasses")

class HumanPlayer(Player):
    def make_move(self,board):
        while True:
            X = int(input(f"{self.name}, choose you position x 0 - 8: "))
            Y = int(input(f"{self.name}, choose you position y 0 - 8: "))
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[X][Y] == 'NaN':
                        board[X][Y] = self.marker
                        break
                    else:
                        print("This position is already taken. Choose another.")
# player class for computer 
class ComputerPlayer(Player):
    def make_move(self,board):
        while True:
            avaliable = []
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == 'NaN':
                        avaliable.append((row,col))
            x,y = random.choice(avaliable)
            board[x][y] = self.marker
            print(f"{self.name} (computer) chose position {(x,y)}")



