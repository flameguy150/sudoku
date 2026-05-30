'''for music'''
import pygame
import os
import sys
import time
import random
from src.neo.config import globals
from src.neo.core.board import _board





def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



### ↓↓↓ MUSIC ↓↓↓ ###### ↓↓↓ MUSIC ↓↓↓ ###### ↓↓↓ MUSIC ↓↓↓ ### 
def mute_music():
    '''
    should mute music if has volume
    should unmute music if has no volume
    use global flag 
    '''
    if globals.mute_flag == True:
        globals.SUDOKU_DJ.set_volume(0)
    elif globals.mute_flag == False:
        globals.SUDOKU_DJ.set_volume(globals.volume)




### ↓↓↓ DISPLAY ↓↓↓ ###### ↓↓↓ DISPLAY ↓↓↓ ###### ↓↓↓ DISPLAY ↓↓↓ ### 
def display_w_h():
    custom_text = globals.cf_small.render(f"{globals.WIDTH} x {globals.HEIGHT}", True, (0, 0, 0)) # Green text

    globals.screen.blit(custom_text, (0, globals.HEIGHT - globals.HEIGHT/15)) 

def start_time():
    """
    Starts time once player enters game
    """
    globals.timer_.start()

def stop_time():
    globals.timer_.stop()


def display_time():
    """ Display elapsed time during in-game screen """
    elapsed_seconds = 0
    if globals.timer_ is not None:
        elapsed_seconds = int(globals.timer_.elapsed())

    minutes, seconds = divmod(elapsed_seconds, 60)
    custom_text = globals.cf_small.render(f"{minutes:02}:{seconds:02}", True, (0, 0, 0))

    globals.screen.blit(custom_text, (0, 0))

def display_mistakes():
    """ Display mistakes during in-game screen """
    custom_text = globals.cf_small.render(f"Mistakes: {globals.mistakes}", True, (0, 0, 0))

    globals.screen.blit(custom_text, (globals.WIDTH - globals.WIDTH/4, 0)) 


def resize_font():
    normal = globals.WIDTH//25
    small = globals.WIDTH//30
    # globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
    # globals.cf_small = pygame.font.Font('assets/fonts/FSEX300.TTF', small)

    globals.custom_font = pygame.font.Font('assets/fonts/JetBrainsMonoNerdFont-ExtraLightItalic.ttf', normal)
    globals.cf_small = pygame.font.Font('assets/fonts/JetBrainsMonoNerdFont-ExtraLightItalic.ttf', small)





### ↓↓↓ GAME FUNCTIONS ↓↓↓ ###### ↓↓↓ GAME FUNCTIONS ↓↓↓ ###### ↓↓↓ GAME FUNCTIONS ↓↓↓ ###  

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
    """
    After the a full board is generated (the solution), we hide some cells to make it a puzzle.
    How many cells depends on the difficulty settings.

    Args:
        diff : difficulty setting (easy, medium, hard)
    """
    random_cells = [ ]
    # n = 0
    # if diff == "easy":
    #     n = 24

    # elif diff == "medium":
    #     n = 32

    # elif diff == "hard":
    #     n = 40

    # index = 82 - n

    # # populate cell with n values
    # for i in range(n):
    #     random_cells.append(i)

    # # add or subtract random amount for each value // maxed at 59
    # for i in range(len(random_cells)):
    #     x = random.randint(0, 82-n) # random value to add
    #     random_cells[i] += x

    random_cells = [0]  # THIS IS FOR DEBUGGING  
    # now we insert the randomized cells to be skipped in the drawing process into our global variable to be used in the cell.py file  
 
    globals.random_cells = random_cells
