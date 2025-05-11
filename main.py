import bestFirstSearch
import board
import player

class playGame():
    def playGame():
        print("Welcome to Tic Tac Toe!")
        gameBoard = board.board()
        user = player.player()
        ai = bestFirstSearch.bestFirstSearch()
            
        if(user.getSymbol() == 1):
            #Player starts first
            current_player = user.getSymbol()
            gameBoard.printBoard() 
        else:
            #Computer starts first
            current_player = 1
            # gameBoard.printBoard() 

        while True:
            if current_player == user.getSymbol():
                while True:
                    try:
                        move = input("Enter your move as 'row col' (e.g. 1 1)")
                        row, col = map(int, move.strip().split())
                        if gameBoard.makeMove(row, col, user.getSymbol()):
                            break
                        else:
                            print("Cell already choosen. Try again")
                    except ValueError:
                        print("Invalid input")
            else:
                print("Computer is making a move...")
                gameBoard = ai.bestFirstSearch(gameBoard, user.getOpponent())

            gameBoard.printBoard()

            result = gameBoard.determineWinner()
            if result is not None:
                if result == user.getSymbol():
                    print("You WON!!!")
                elif result == user.getOpponent():
                    print("Computer won. You LOST!!")
                else:
                    print("Its a draw")
                break
                
            current_player = user.getOpponent() if current_player == user.getSymbol() else user.getSymbol()

if __name__ == "__main__":
    playGame.playGame()