'''for music'''
import os
import sys
import random
from src.neo.config import globals
from src.neo.core.board import _board
import pygame



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def mute_music():
    '''
    should mute music if has volume
    should unmute music if has no volume
    use global flag 
    '''
    if globals.mute_flag == True:
        globals.SUDOKU_DJ.set_volume(0)
    elif globals.mute_flag == False:
        globals.SUDOKU_DJ.set_volume(0.7)

def display_w_h():
    custom_text = globals.cf_small.render(f"{globals.WIDTH} x {globals.HEIGHT}", True, (0, 0, 0)) # Green text

    globals.screen.blit(custom_text, (0,0)) 

def resize_font():
    normal = globals.WIDTH//25
    small = globals.WIDTH//30
    # globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
    # globals.cf_small = pygame.font.Font('assets/fonts/FSEX300.TTF', small)

    globals.custom_font = pygame.font.Font('assets/fonts/JetBrainsMonoNerdFont-ExtraLightItalic.ttf', normal)
    globals.cf_small = pygame.font.Font('assets/fonts/JetBrainsMonoNerdFont-ExtraLightItalic.ttf', small)

def remake_puzzle():
    """
    generate new puzzle for new game here
    """
        
    #generate solution through array
    globals.board = _board() 
    #then put that solution in globals.board and then generate the baord using the solution
    #keeping some cells hidden 
    globals.grid._createsolution(globals.board)
    globals.grid.generate_board(globals.board)

def hide_cells(diff):
    random_cells = [ ]
    n = 0
    if diff == "easy":
        n = 24

    elif diff == "medium":
        n = 32

    elif diff == "hard":
        n = 40

    index = 82 - n

    # populate cell with n values
    for i in range(n):
        random_cells.append(i)

    # add or subtract random amount for each value // maxed at 59
    for i in range(len(random_cells)):
        x = random.randint(0, 82-n) # random value to add
        random_cells[i] += x

        
    # now we insert the randomized cells to be skipped in the drawing process into our global variable to be used in the cell.py file  
 
    globals.random_cells = random_cells