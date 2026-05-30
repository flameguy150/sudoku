''' 
revamping sudoku
old code was unreadable and unorganized
goals for this version:
    - cleaner code, OOP still but with less global variable mess, solidified grid class
    - different screens
    - options
All will be stored in neo folder under src

GLOBAL VARIABLES IN src.neo.config
'''
import pygame
from pygame import mixer
import os
from src.neo.config.constants import WHITE, BLACK, FPS
from src.neo.config import globals
from src.neo.ui.gameState import gameStateManager
from src.neo.core.grid import Grid
from src.neo.utils.utilities import resource_path, mute_music, display_w_h, resize_font, remake_puzzle, hide_cells, save_game, load_game
from src.neo.utils.timer import Timer
from src.neo.ui.flower import Flower


pygame.init()

# Icon
icon_image = pygame.image.load('assets/art/icon/icon_256.png') 
pygame.display.set_icon(icon_image)

#flower sprite init
globals.flower = pygame.sprite.Group()
_flower = Flower((globals.WIDTH/24)*11, (globals.HEIGHT/24)*11) #tried to center as much as possible lol
globals.flower.add(_flower)
# Set up display dimensions
globals.screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("sudoku")

#----MUSIC--------------------------------------------------------------------
song = resource_path(os.path.join("assets/sounds", "flowers.mp3"))

globals.mute_flag = False
mixer.init() 
globals.SUDOKU_DJ = mixer.music

# Configure and play music
globals.SUDOKU_DJ.load(song) 
globals.SUDOKU_DJ.set_volume(globals.volume) 
globals.SUDOKU_DJ.play(-1, 0.0) 
#----INIT--------------------------------------------------------------------
clock = pygame.time.Clock()
normal = globals.WIDTH//25
small = globals.WIDTH//30


# globals.font_number_size = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
# globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
# globals.cf_small = pygame.font.Font('assets/fonts/FSEX300.TTF', small)


globals.custom_font = pygame.font.Font('assets/fonts/JetBrainsMonoNerdFont-ExtraLightItalic.ttf', normal)
globals.cf_small = pygame.font.Font('assets/fonts/JetBrainsMonoNerdFont-ExtraLightItalic.ttf', small)




# Game loop--------------------------------------------------------------------
globals.running = True
globals.screen.fill(BLACK)  # Fill the background with black

game = gameStateManager()
#runs and loads up main menu
game.run() 

#Init grid here
globals.grid = Grid() 


# INIT THE RANDOM CELLS TO BE DRAWN HERE
# --------------------------------
# depending on settings, we can make change how many cells are drawn
# 81 * .3 = 24.3 = 24 (EASY) 57
# 81 * .4 = 32.4 = 32 (MEDIUM) 49
# 81 * .5 = 40.5 = 41 (HARD) 40
# depending on difficulty, i will set the number and decrement by 1 

# (EASY) --------------------------------------------------------------------
"""
depending on "easy", "medium", or "hard", it will determine how many of the cells are covered
"""

globals.difficulty = "easy" 
# --------------------------------



# we init cell grid in order to store cells

globals.cell_grid = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
      for j in range(9):
            index = i * 9 + j
            globals.cell_grid[i][j] = globals.grid.array_of_cells[index]


#remake_puzzle() generates the solution and the puzzle. It is called remake_puzzle because it will be used again if the player wants to start a new game after winning
remake_puzzle()

globals.grid.print_grid_array() #debug
globals.grid.print_answer()
while globals.running:
    globals.curr_event = None

    # ----EVENT HANDLING--------------------------------------------------------
    for event in pygame.event.get():
        globals.curr_event = event
        
        if event.type == pygame.QUIT:
            save_game()
            globals.running = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                     globals.mute_flag = not globals.mute_flag
                     mute_music()
                ## DEBUGGING ↓
                if event.key == pygame.K_f:
                      globals.screen_info = not globals.screen_info
                if event.key == pygame.K_o:
                      globals.grid.print_current_board()
                if event.key == pygame.K_l:
                      load_game()


        # FOR WINDOW RESIZE ↓
        elif event.type == pygame.VIDEORESIZE:
                # Update screen dimensions and recreate the display surface
                globals.WIDTH, globals.HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT), pygame.RESIZABLE)
                #grid resizes w window resize
                globals.grid.resize_array()
                #font resizes w window resize
                resize_font() 
                pygame.display.flip()
        globals.grid.check_solution()
                
        game.get_input(event)
    


    game.run()
    if globals.screen_info == True:
            display_w_h() #display width and height in top left corner
    pygame.display.flip()
    clock.tick(FPS)



    #-----DRAWING--------------------------------------------------
    

    # -------------------------------------------------------------
    


