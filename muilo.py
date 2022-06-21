# printing the game board
import random
import time
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']





winner = None
gameRunning = True


def currentPlayer():
    Player = None
    choose = True
    while choose:
        inp = input('Declare side by typing 1 for X side, 2 for 0 side or 3 to let the random choice: ')
        while not inp.isdigit():
            print( )
            inp = input('Sorry, but the number that u choose is not correct. \nDeclare side by typing 1 for X side, 2 for 0 side or 3 to let the random choice: ')
        inp = int(inp)
        if inp == 1 or inp == 2 or inp == 3:
            if inp == 1:
                Player = "X"
                choose = False
                return Player
    
            elif inp == 2:
                Player = '0'
                choose = False
                return Player
    
            elif inp == 3:
                Player = random.choice(['X', '0'])
                choose = False
                return Player
        else:
            choose = True
      

a = currentPlayer()
print( )
print('U are: ', a)
print( )
def typingCompSide():
    if a == 'X':
        return '0'

    elif a == '0':
        return 'X'


b = typingCompSide()

# gameboard

def printBoard():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    # print("--------------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    # print("--------------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")





# printBoard()

# take player input
def playerInput():
    z = 0
    while z == 0:
        inp = input('Choose a spot from 1-9: ')
        while not inp.isdigit():
            print( )
            inp = input('U should choose number from a spot 1-9: ')
        inp = int(inp)
        # while inp > 9:
        #     inp = input('U should choose number from a spot 1-9: ')
        if 1 <= inp <= 9 and board[inp - 1] == ' ':
            board[inp - 1] = a
            z = 1
        else:
            print("Oops! Spot not avalible or out of range")
            z = 0




def computerMove():
    time.sleep(1)
    k = random.randint(0,8)
    while board[k] != ' ':
            k = random.randint(0,8)
    board[k] = b



# check for win or tie
def checkHorizontal(board):
    global winner

    if board[0] == board[1] == board[2] != ' ':
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] != ' ':
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] != ' ':
        winner = board[8]
        return True


def checkVertical(board):
    global winner

    if board[0] == board[3] == board[6] != ' ':
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] != ' ':
        winner = board[4]
        return True
    if board[3] == board[5] == board[8] != ' ':
        winner = board[8]
        return True


def checkDiagonal(board):
    global winner

    if board[0] == board[4] == board[8] != ' ':
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != ' ':
        winner = board[4]
        return True


def CheckIfWin(board):
    global gameRunning
    

    if checkHorizontal(board):
        print('The winner is: ', winner)
        gameRunning = False

    elif checkVertical(board):
        print('The winner is: ', winner)
        gameRunning = False

    elif checkDiagonal(board):
        print('The winner is: ', winner)
        gameRunning = False

    elif ' ' not in board:
          print('It\'s a tie')
          gameRunning = False

    


# switch the player


# def SwitchPlayer():
#     global currentPlayer
#
#     if currentPlayer == 'X':
#         currentPlayer = '0'
#     else:
#         currentPlayer = 'X'


# check for win or tie again



while gameRunning:
    if a == '0':
        
        print('Computer move..')
        computerMove()
        printBoard()
        CheckIfWin(board)
        if gameRunning:
          playerInput()
          printBoard()
          CheckIfWin(board)
    else:
        printBoard()
        playerInput()
        printBoard()
        CheckIfWin(board)
        if gameRunning:
          print('Computer move..')
          computerMove()
          #printBoard()
          CheckIfWin(board)
    #SwitchPlayer()
