import pygame
import random

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


def create_puzzle(board): #recursive backtracking algorithm
    numbers = list(range(1,10)) #list of numbers from 1 - 10
    for row in range(9):
        random.shuffle(numbers)
        for column in range(9):
            if board[row][column] == 0:

                for num in numbers:
                    if is_valid(board, row, column, num):
                        board[row][column] = num

                        if create_puzzle(board):
                            return True #this will activate if the board is solved
                        
                        board[row][column] = 0

                return False #when reaching false, it backtracks one level up ad starts again
    return True



def printboard(board):
    string = ""
    for row in range(9):
        string += "\n" + "-------------------------\n"
        
        for x in range(3):
            string+="| "
            for xx in range(3):
                c = ((xx) + (x*3))
                string += str(board[row][c]) + " "
                if xx == 2 and x == 2:
                    string += "|"
    print(string)
    
def _board():
    board = [[0] * 9 for _ in range(9)]

    board[0][0] = random.randint(0,9) #so the puzzle is different every time

    create_puzzle(board)
    
    # printboard(board)
    return board