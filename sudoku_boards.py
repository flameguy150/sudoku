import pygame
import random
import sys
# sys.setrecursionlimit(1500)

#sudoku boards

easygrid1_ = [[0, 7, 0, 0, 2, 0, 0, 4, 6],
			  [0, 6, 0, 0 ,0 ,0, 8, 9, 0],
			  [2, 0, 0, 8, 0 ,0 ,7, 1, 5],
			  [0, 8, 4, 0, 9, 7, 0, 0, 0],
			  [7, 1, 0, 0, 0, 0, 0, 5, 9],
			  [0, 0, 0, 1, 3, 0, 4, 8, 0],
			  [6, 9, 7, 0, 0, 2, 0, 0, 8],
			  [0, 5, 8, 0, 0, 0, 0, 6, 0],
			  [4, 3, 0, 0, 8, 0, 0, 7, 0]
			  ]
easygrid1_solution = [[8, 7, 5, 9, 2, 1, 3, 4, 6],
		[3, 6, 1, 7, 5, 4, 8, 9, 2], 
		[2, 4, 9, 8, 6, 3, 7, 1, 5], 
		[5, 8, 4, 6, 9, 7, 1, 2, 3],
		[7, 1, 3, 2, 4, 8, 6, 5, 9],
		[9, 2, 6, 1, 3, 5, 4, 8, 7],
		[6 ,9, 7, 4, 1, 2, 5, 3, 8],
		[1, 5, 8, 3, 7, 9, 2, 6, 4],
		[4, 3, 2, 5, 8, 6, 9, 7, 1]
		]


"""
    we can try to create it manually w for loops or

    we can use random.shuffle until each row is different from each other?

    need to wrap the for loop up in another for loop of 9 times

    now we just need to ensure that before we append an element to row, 
    previous rows do not have that same number in the same index

    we also need to ensure that there are no more than 1 of each number in a "cell"
    
    each cell has no more than 9 blocks
"""
cell1 = [ (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2) ]
cell2 = [ (0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5) ]
cell3 = [ (0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8) ]
cell4 = [ (3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2) ]
cell5 = [ (3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5) ]
cell6 = [ (3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8) ]
cell7 = [ (6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2) ]
cell8 = [ (6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5) ]
cell9 = [ (6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8) ]

cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

def is_valid(board, row, column, num): #boolean function that returns true if is valid
    """first, need to identify which cell the num is located on the grid
    then, check if the number already exists within that cell
    then check if number exists in the row and column
    """

    start_row = row//3 * 3
    start_col = column//3 * 3
    
    for x in range(3):
        for y in range(3):
            if board[start_row + x][start_col + y] == num:
                return False
            
            
    #check rows
    for r in range(9):
        if board[row][r] == num:
            return False
        
    #check columns
    for c in range(9):
        if board[c][column] == num:
            return False
        
    #if the func passes to here, the solution is valid!
    return True


def solution(board): #recursive backtracking algorithm
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:

                for num in range(1,10):
                    if is_valid(board, row, column, num):
                        board[row][column] = num

                        if solution(board):
                            return True #this will activate if the board is solved
                        
                        board[row][column] = 0

                return False #when reaching false, it backtracks one level up ad starts again
    return True

def create_puzzle():
    # after getting a solved board, should make a puzzle out of it by taking away some numbers
    #easy
    #med
    #hard - takes a whole set of numbers (like all 9s), each cell has 5 nums max
    pass
    
def _board():
    board = [[0] * 9 for _ in range(9)]

    board[0][0] = random.randint(0,9) #so the puzzle is different every time

    solution(board)
    
    printboard(board)
    return board

def printboard(board):
    string = ""
    for row in range(9):
        string += "\n" + "-----------------------\n"
        
        for x in range(1,4):
            string+="| "
            for xx in range(3):
                c = ((xx) + x)
                string += str(board[row][c]) + " "
    print(string)







"""
def oldgenerateboard():
    board = []
    row = []
    curr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tmp = random.choice(curr)
    for x in range(9):
        for i in range(9):
            while tmp in row: #if tmp already exists, need to change it to another number after noting it has been used
                curr.remove(tmp)
                tmp = random.choice(curr)
            row.append(tmp)
        #after its done creating a row, curr should be reset, row should be appended and then reset
        curr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        board.append(row)
        row = []
    print(board)#printing!

def is_valid(board, row, column, num): #boolean function that returns true if is valid
    #check rows
    for r in range(9):
        if board[row][r] == num:
            return False
        
    #check columns
    for c in range(9):
        if board[c][column] == num:
            return False

    curr_cell = None
    for cell in cells:
        for x in range(9):
                if (row,cell) == cell[x]:#if the [row][cell] spot exists in the cell, that means that spot belongs to that cell
                    curr_cell = cell #get the current cell and that check every spot in that cell if the num exists
                    break
    if curr_cell is None:
        raise ValueError(f"Cell not found for row={row}, column={column}. Check cell definitions.")
    
    for (r,c) in curr_cell:
        if board[r][c] == num: #if the target num already exists within the cell, the num is not valid
            return False
        
    #if the func passes to here, the solution is valid!
    return True

"""