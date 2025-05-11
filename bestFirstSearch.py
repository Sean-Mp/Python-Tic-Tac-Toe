#Best first search algorithm, along with determininstic
import board
from random import randrange

class bestFirstSearch():

    def bestFirstSearch(self, start, player):
        # Implement the best first search algorithm here

        #Base case, no moves have been made
        if self.isEmpty(start):
            cornerRandom = randrange(4)
            if cornerRandom == 0:
                start.makeMove(0,0,player)
            elif cornerRandom == 1:
                start.makeMove(0,2,player)
            elif cornerRandom == 2:
                start.makeMove(2,0,player)
            elif cornerRandom == 3:
                start.makeMove(2,2,player)
            return start
            
        open = [start]
        close = []
        while open != []:
            node = open.pop(0)
            
            if node.determineWinner() == 1 or node.determineWinner() == 0:
                return node
            else:
                children = self.generateChildren(node, player)
                for child in children:
                    if child not in open and child not in close:
                        child.heuristic = self.calculateHeuristic(child, player)
                        open.append(child)
                    elif child in open:
                        if child.heuristic < open[open.index(child)].heuristic:
                           open[open.index(child)] = child
                close.append(node)
                open.sort(key=lambda x: x.heuristic)
                return open[0]
            
        # if close:
        #     return close[-1]
        return start
    
    def generateChildren(self, currentBoard, player):
        # Generate all possible children of the current board state
        # For each empty cell, create a new board state with the current player making a move
        children = []

        for i in range(currentBoard.rows):
            for j in range(currentBoard.cols):
                if currentBoard.ticTacToe[i][j] == 0:
                    newBoard = board.board()
                    newBoard.ticTacToe = [row[:] for row in currentBoard.ticTacToe]
                    newBoard.makeMove(i, j, player)
                    children.append(newBoard)
        return children
    
    def calculateHeuristic(self, node, player):
        # Calculate the heuristic value for the node
        # If heuristuc is -inf, then its a winning state for the computer
        # If heuristic is inf, then its a winning state for the player
        # If heuristic is 0, then its a draw state
        # Else any value > 0 represents the number of X's or O's needed to win, e.g if heuristic is 1, then one more X or O is needed to win
        if node.determineWinner() == 1:
            return float('-inf')
        elif node.determineWinner() == -1:
            return float('inf')
        elif node.determineWinner() == 0:
            return 0
        else:
            # Calculate the heuristic based on the number of player symbol needed to win
            # If no winning moves, check for blocking moves
            for i in range(node.rows):
                for j in range(node.cols):
                    if node.ticTacToe[i][j] == 0:
                        node.ticTacToe[i][j] = -player
                        if node.determineWinner() == -player:
                            node.ticTacToe[node.lastMove[0]][node.lastMove[1]] = 0
                            node.ticTacToe[i][j] = player 
                            return -1
                        node.ticTacToe[i][j] = 0

            # first determine if there are any winning moves for the player
            for i in range(node.rows):
                for j in range(node.cols):
                    if node.ticTacToe[i][j] == 0:
                        node.ticTacToe[i][j] = player
                        if node.determineWinner() == player:
                            node.ticTacToe[node.lastMove[0]][node.lastMove[1]] = 0
                            node.ticTacToe[i][j] = player
                            return 1
                        node.ticTacToe[i][j] = 0
            # Determine if there is a move which results in 2 X's or O's in a row
            #Check if player is in corner
            corner = self.isInCorner(node, player)
            if corner != False:
                #check if any move in the next row, col or diag results in 2 X's or O's in a row
                if corner == [0,0] or corner == [2,0]:   #right and middle
                    if node.ticTacToe[1][1] == 0 or node.ticTacToe[0][1] == 0 or node.ticTacToe[2][1] == 0:
                        return 3
                elif corner == [0,2] or corner == [2,2]: #left and middle
                    if node.ticTacToe[1][1] == 0 or node.ticTacToe[0][1] == 0 or node.ticTacToe[2][1] == 0:
                        return 3
                elif corner == [0,0] or corner == [0,2]: #down
                    if node.ticTacToe[1][0] == 0 or node.ticTacToe[1][2] == 0:
                        return 3
                elif corner == [2,0] or corner == [2,2]: #up
                    if node.ticTacToe[1][0] == 0 or node.ticTacToe[1][2] == 0:
                        return 3
            #Check if player is in middle
            middle = self.isInMiddle(node, player)
            if middle != False:
                for i in range(node.rows):
                    if( node.ticTacToe[i][0] == 0 or node.ticTacToe[i][1] == 0 or node.ticTacToe[i][2] == 0):
                        return 4
            #Check if player is in side
            side = self.isInSide(node, player)
            if side != False:
                if side == [1,0]:
                    if node.ticTacToe[0][0] == 0 or node.ticTacToe[2][0] == 0 or node.ticTacToe[1][1]:
                        return 5
                elif side == [1,2]:
                    if node.ticTacToe[0][2] == 0 or node.ticTacToe[2][2] == 0 or node.ticTacToe[1][1]:
                        return 5
                elif side == [2,1]:
                    if node.ticTacToe[2][0] == 0 or node.ticTacToe[2][2] == 0 or node.ticTacToe[1][1]:
                        return 5
                elif side == [0,1]:
                    if node.ticTacToe[0][0] == 0 or node.ticTacToe[0][2] == 0 or node.ticTacToe[1][1]:
                        return 5
            # Try to get a random corner if no other moves are available
            randomCorner = randrange(4)
            if randomCorner == 0:
                if node.ticTacToe[0][0] == 0:
                    return 6
            elif randomCorner == 1:
                if node.ticTacToe[0][2] == 0:
                    return 6
            elif randomCorner == 2:
                if node.ticTacToe[2][0] == 0:
                    return 6
            elif randomCorner == 3:
                if node.ticTacToe[2][2] == 0:
                    return 6
            # If no other moves are available, return a random move

            if self.atLeastOneCellOpen(node):
                while True:
                    randomMove = randrange(9)
                    if node.ticTacToe[randomMove//3][randomMove%3] == 0:
                        return 7
            else:
                return 10
    
    def isInCorner(self, board, player):
        if(board.ticTacToe[0][0] == player):
            return [0,0]
        elif(board.ticTacToe[0][2] == player):
            return [0,2]
        elif(board.ticTacToe[2][0] == player):
            return [2,0]
        elif(board.ticTacToe[2][2] == player):
            return [2,2]
        return False
    def isInMiddle(self, board, player):
        if(board.ticTacToe[1][1] == player):
            return [1,1]
        return False
    def isInSide(self, board, player):
        if(board.ticTacToe[0][1] == player):
            return [0,1]
        elif(board.ticTacToe[1][0] == player):
            return [1,0]
        elif(board.ticTacToe[1][2] == player):
            return [1,2]
        elif(board.ticTacToe[2][1] == player):
            return [2,1]
        return False
    def atLeastOneCellOpen(self, board):
        #Check of the board has at least one empty cell
            for i in range(board.rows):
                for j in range(board.cols):
                    if(board.ticTacToe[i][j] == 0):
                        return True
            return False
    def isEmpty(self, board):
        for i in range(board.rows):
            for j in range(board.cols):
                if(board.ticTacToe[i][j] != 0):
                    return False
        return True