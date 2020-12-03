# Alden Maben
# CSCI 4849

# This two player game can be played using only two buttons. One to navigate(l button) and one to select(enter button).

#Cited Sources
# Heavily relied on this Connect4 tutorial "https://medium.com/@geoffrey.mariette/crazy-connect4-with-python-146d384f4cfb" for building the board and general game rule functionality
# To get diagonal win detection working I used this reference "https://stackoverflow.com/questions/38436732/diagonal-wins-arent-being-detected-python".
class ModifiedConnect4:

    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.board = [ [ '  ' for _ in range( self.cols)] for _ in range(self.rows) ]
        
    def __del__(self):
        print("Creating New Game...")

    def printBoard(self): # Prints the Board
        for i, j in enumerate(self.board):
            print("_" * ((self.cols * 4)+5)) # prints horizontal lines
            print(*j, sep=' | ') # prints vertical lines
        print('    '.join(str(x) for x in range(self.cols))) # spacing
        
    def player_input(self): # Select player pieces
        player1 = input("Please pick your player 'X' or 'O' ")
        if player1 == 'l':
            player1 = 'X'
        elif player1 =='ll':
            player1 = 'O'
        else:
            print('Failed')
            player1 = input("Please pick your weapon 'X' or 'O' ")
        while True:
            if player1.upper() == 'X':
                player2='O'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                return player1.upper(),player2
            elif player1.upper() == 'O':
                player2='X'
                print("You've choosen " + player1 + ". Player 2 will be " + player2)
                return player1.upper(),player2
            else:
                print("Failed")
                player1 = input("Please pick your weapon 'X' or 'O' ")

    def isAvailable(self, row, column): # Checks availability of spot on board
        if row[column] == '  ':
            return True
        return False
    
    def playableOption(self, playercolumn, piece):
        for i in reversed(self.board):
            if self.isAvailable(i, playercolumn):
                i[playercolumn] = " " + piece
                return True
        return False

    def player_choice(self): # Column choices for player
        choice = input("Please select an empty space between 0 and 6 : ")
        if choice=='l':
            choice = 0
        elif choice=='ll':
            choice = 1
        elif choice=='lll':
            choice = 2
        elif choice=='llll':
            choice = 3
        elif choice=='lllll':
            choice = 4
        elif choice=='llllll':
            choice = 5
        elif choice=='lllllll':
            choice = 6
        else:
            print('Failed')
        while self.board[0][choice] != '  ':
            #print("Inside")
            choice=self.player_choice() #using recurssion to make sure to get a correct response
        return choice

    def generateReversedBoard(self): # Used to switch coordinates to check for 4 in a row  
        reversedBoard = []
        for l in self.board:
            for index, place in enumerate(l):
                try:
                    reversedBoard[index].append(place)
                except:
                    reversedBoard.append([])
                    reversedBoard[index].append(place)
        return reversedBoard
    
    
    def lineWin(self, piece, board=None): #Check for 4 in a row or column
        if board is None:
            board=self.board
        for l in board:
            for i in range(0,len(l)):
                if i < len(l) - 3:
                    if l[i] == l[i+1] == l[i+2] == l[i+3] == " " + piece:
                        return True
                    

    def Diagonals(self, piece):
        diagBoard = []
        for i, j in enumerate(self.board):
            for k, place in enumerate(j):
                if place == ' ' + piece:
                    diagBoard.append(int(str(i)+str(k)))

        for place in diagBoard: # check diagonal 4 in a row in '/' form
            if int(place) + 11 in diagBoard and int(place) + 22 in diagBoard and int(place) + 33 in diagBoard:
                return True

        for place in reversed(diagBoard) :# check diagonal 4 in a row in '\' form
            if int(place) - 9 in diagBoard and int(place) - 18 in diagBoard and int(place) - 27 in diagBoard:
                return True


game = True
connect = ModifiedConnect4()
while game==True:
    print("")
    print("Welcome to Modyfied Connect4! Use l to navigate options and hit enter to select")
    players = connect.player_input()
    connect.printBoard()
    winner = False
    i = 1
    while not winner: # game still going
        if i % 2 == 0:
            currentPlayer = "Player 1"
            piece = players[1]
        else:
            currentPlayer = "Player 2"
            piece = players[0]
        position = connect.player_choice()
        if not connect.playableOption(position, piece): #Checks if there is an existing piece
            print("Column ", position," is full. Please choose another column.")

        reversedBoard = connect.generateReversedBoard()
        
        if connect.lineWin(piece) or connect.lineWin(piece, reversedBoard) or connect.Diagonals(piece): # Winner detection looking at default board and reversed board
            winner = True
            connect.printBoard()
            print("Game won by ", currentPlayer)
            newGame = input("Do you want to play again (Y/N) ? ")
            if newGame== 'll':
                game = False
                print("Game over.... Goodbye!")
            elif newGame=='l':
                del connect
                connect = ModifiedConnect4()
            else:
                input("Do you want to play again (Y/N) ? ")
            break
        connect.printBoard()
        i += 1 # tracks player turn