#The tic tac toe board, along with checking whether there is a winner or draw

class board:
    #Board initially 0, -1 represents the O and 1 represents the X
    def __init__(self):
        self.rows, self.cols = 3, 3
        self.ticTacToe = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.heuristic = 0
        self.lastMove = []

    #returning 1 if computer wins, 0 if a draw, -1 if player wins
    def determineWinner(self):
        #Check rows, colums and diagonals for a winner
        lines = []

        for i in range(3):
            lines.append(self.ticTacToe[i]) #rows
            lines.append([self.ticTacToe[0][i], self.ticTacToe[1][i], self.ticTacToe[2][i]]) #columns
            lines.append([self.ticTacToe[0][0], self.ticTacToe[1][1], self.ticTacToe[2][2]]) #diagonal 1
            lines.append([self.ticTacToe[0][2], self.ticTacToe[1][1], self.ticTacToe[2][0]])

        for line in lines:
            if all(cell == 1 for cell in line):
                return 1
            elif all(cell == -1 for cell in line):
                return -1
        
        if all(cell != 0 for row in self.ticTacToe  for cell in row):
            return 0 #draw
        return None
    
    def makeMove(self, row, col, player):
        #Make a move on the board
        if self.ticTacToe[row][col] == 0:
            self.ticTacToe[row][col] = player
            self.lastMove = [row,col]
            return True
        return False
    
    def isFull(self):
        for row in self.ticTacToe:
            if 0 in row:
                return False
        return True
    
    def printBoard(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        print('\nBoard:')
        for row in self.ticTacToe:
            print(' | '.join(symbols[cell] for cell in row))
            print('-' * 9)

    def __eq__(self, other):
        if not isinstance(other, board):
            return False
        return self.ticTacToe == other.ticTacToe
    
    def __hash__(self):
          return hash(tuple(tuple(row) for row in self.ticTacToe))