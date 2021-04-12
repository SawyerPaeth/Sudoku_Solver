#Sawyer Paeth
#Due Dec. 7th
#CS 325 Portfolio Project - Sudoku Solver


def checkRow(board, row):

    seenArr = []                #Creates empty array to track non empty squares

    for i in range(0, 9):

        if board[row][i] in seenArr:        #return false if repeat is found
            return False

        if board[row][i] != 0:              #Add new number to array
            seenArr.append(board[row][i])

    return True


def checkCol(board, col):
    seenArray = []              #Creates empty array to track non empty squares

    for i in range(0, 9):

        if board[i][col] in seenArray:      #return false if repeat is found
            return False

        if board[i][col] != 0:
            seenArray.append(board[i][col]) #Add new number to array

    return True


def checkBox(board, sRow, sCol):

    seenArray = []              #Creates empty array to track non empty squares

    for row in range(0, 3):
        for col in range(0, 3):
            current = board[row+sRow][col + sCol]   #set current

            if current in seenArray:                #repeat found in 3x3 return False
                return False

            if current != 0:
                seenArray.append(current)

    return True

def verify(board, row, col):    #Check for repeats in row, column and 3x3 square

    return (checkRow(board, row) and checkCol(board, col) and checkBox(board, row - row%3, col - col%3))

def verifySetUp(board):

    for i in range(0, 9):
        for j in range(0, 9):

            if not verify(board, i, j):     #return False is checkRow, CheckCol or checkBox returns False
                return False
    return True


def checker(row,col,n):

    for i in range(0,9):            #check if newly placed number is a repeat in row
        if board[row][i] == n:
            return False
    for j in range(0,9):            #check if newly placed number is already in column
        if board[j][col] == n:
            return False

    col2 = (col//3) * 3
    row2 = (row//3) * 3

    for k in range(0,3):
        for l in range(0,3):
            if board[row2 + k][col2 + l] == n:      #check if newly placed number already in 3x3 square
                return False

    return True

def find(row, col):               #find squares that are empty
    num_find = 0
    for a in range(0,9):
        for b in range(0,9):
            if board[a][b] == 0:        #check if empty square
                row = a
                col = b
                num_find = 1
                x = [row, col, num_find]
                return x                #return x with location of empty square

    x = [-1, -1, num_find]
    return x

def solveSudoku():

    row = 0
    column = 0

    x = find(row,column)  #call num remove on 0,0

    if x[2] == 0:
        return True

    row = x[0]
    column = x[1]

    for n in range(1,10):       #check through integers 1-9

        if checker(row, column, n) == True:     #check if current n can be placed
            board[row][column] = n

            if solveSudoku():                   #return True if solver works
                return True

            board[row][column] = 0

    return False


board = [[0, 0, 0, 0, 0, 9, 0, 7, 8],
        [0, 0, 0, 7, 0, 0, 9, 0, 0],
        [5, 0, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 3, 0, 7, 0, 0, 8, 0],
        [0, 2, 5, 0, 8, 0, 7, 6, 0],
        [0, 9, 0, 0, 5, 0, 4, 0, 0],
        [1, 0, 0, 0, 9, 0, 0, 0, 5],
        [0, 0, 4, 0, 0, 3, 0, 0, 0],
        [9, 3, 0, 4, 0, 0, 0, 0, 0]]


if verifySetUp(board):

    if solveSudoku() == True:
        print('Solution:')
        for x in range(0,9):
            print(board[x])
    else:
        print("No solution possible")

else:
    print("Input board is not valid.")