board = [' ' for x in range(10)]

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

# print(board)
# printBoard(board)
def insertLetter(letter, pos):
    board[pos] = letter
    
def spaceIsFree(pos):
    return board[pos] == ' '

def isBoardFull(baord):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1 - 9): ")
        try:
            move = int(move)
            if move > 0 and move <10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')

            else:
                print('Please type a number within the range(1-9)')

        except: 
            print('Please type a number!')

def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l)
            or (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or 
            (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or 
            (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l))

import random as r

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(cornersOpen) > 0:
        move = r.choice(cornersOpen)
        return move

    elif len(edgesOpen) > 0:
        move = r.choice(edgesOpen)
        return move

    elif 5 in possibleMoves:
        move = 5
        return move
    
    return move

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time!")
            break
        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print("Tie Game!")
            else:
                insertLetter('O', move)
                print("Computer placed an 'O' in position", move, ':')
                printBoard(board)
        else:
            print("X's won this time! Good Job!")
            break

    if isBoardFull(board):
        print("Tie Game!")


while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break