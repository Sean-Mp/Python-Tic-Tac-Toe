class player():
    #Player class to choose the player and make moves
    def __init__(self):
        self.playerSymbol = 0 
        self.choosePlayer()
    
    def choosePlayer(self):
        #Choose the player for the game
        while True:
            choice = input("Choose your symbol (X or O): ").strip().upper()
            if choice == 'X':
                self.playerSymbol =1 
                print("You are X. The computer is O")
                break
            elif choice == 'O':
                self.playerSymbol = -1
                print("You are O. The computer is X")
                break
            else:
                print("Invalid choice. Please enter X or O")
        
    def getSymbol(self):
        return self.playerSymbol
    
    def getOpponent(self):
        if self.playerSymbol == 1:
            return -1
        elif self.playerSymbol == -1:
            return 1
        
    def isFirst(self):
        if self.playerSymbol == 1:
            return False
        return True