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
import sys
import time
from src.neo.config.constants import WHITE, BLACK, FPS
from src.neo.config import globals
from src.neo.ui.gameState import gameStateManager
from src.neo.core.grid import Grid
from src.neo.utils.utilities import resource_path, mute_music, display_w_h, resize_font
from src.neo.ui.flower import Flower
from src.neo.core.board import _board

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
globals.SUDOKU_DJ.set_volume(0.7) 
globals.SUDOKU_DJ.play(-1, 0.0) 
#----INIT--------------------------------------------------------------------
clock = pygame.time.Clock()
normal = globals.WIDTH//25
small = globals.WIDTH//30
globals.font_number_size = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
globals.cf_small = pygame.font.Font('assets/fonts/FSEX300.TTF', small)




# Game loop--------------------------------------------------------------------
globals.running = True
globals.screen.fill(BLACK)  # Fill the background with black
game = gameStateManager()
#runs and loads up main menu
game.run() 
#Init grid here
globals.grid = Grid() 

# we init cell grid in order to store cells
globals.cell_grid = [[globals.grid.array_of_cells[0] ,globals.grid.array_of_cells[1], globals.grid.array_of_cells[2], globals.grid.array_of_cells[27], globals.grid.array_of_cells[28], globals.grid.array_of_cells[29], globals.grid.      array_of_cells[54], globals.grid.array_of_cells[55], globals.grid.array_of_cells[56]],
			 [globals.grid.array_of_cells[3], globals.grid.array_of_cells[4], globals.grid.array_of_cells[5], globals.grid.array_of_cells[30] ,globals.grid.array_of_cells[31], globals.grid.array_of_cells[32], globals.grid.array_of_cells[57], globals.grid.array_of_cells[58], globals.grid.array_of_cells[59]],
			 [globals.grid.array_of_cells[6], globals.grid.array_of_cells[7], globals.grid.array_of_cells[8], globals.grid.array_of_cells[33], globals.grid.array_of_cells[34], globals.grid.array_of_cells[35], globals.grid.array_of_cells[60], globals.grid.array_of_cells[61], globals.grid.array_of_cells[62]],
			 [globals.grid.array_of_cells[9], globals.grid.array_of_cells[10], globals.grid.array_of_cells[11], globals.grid.array_of_cells[36], globals.grid.array_of_cells[37], globals.grid.array_of_cells[38], globals.grid.array_of_cells[63 ], globals.grid.array_of_cells[64], globals.grid.array_of_cells[65]],
			 [globals.grid.array_of_cells[12],globals.grid.array_of_cells[13], globals.grid.array_of_cells[14], globals.grid.array_of_cells[39], globals.grid.array_of_cells[40], globals.grid.array_of_cells[41], globals.grid.array_of_cells[66], globals.grid.array_of_cells[67], globals.grid.array_of_cells[68]],
			 [globals.grid.array_of_cells[15],globals.grid.array_of_cells[16], globals.grid.array_of_cells[17], globals.grid.array_of_cells[42], globals.grid.array_of_cells[43], globals.grid.array_of_cells[44], globals.grid.array_of_cells[69], globals.grid.array_of_cells[70], globals.grid.array_of_cells[71]],
			 [globals.grid.array_of_cells[18],globals.grid.array_of_cells[19], globals.grid.array_of_cells[20], globals.grid.array_of_cells[45], globals.grid.array_of_cells[46], globals.grid.array_of_cells[47], globals.grid.array_of_cells[72], globals.grid.array_of_cells[73], globals.grid.array_of_cells[74]],
			 [globals.grid.array_of_cells[21],globals.grid.array_of_cells[22], globals.grid.array_of_cells[23], globals.grid.array_of_cells[48], globals.grid.array_of_cells[49], globals.grid.array_of_cells[50], globals.grid.array_of_cells[75], globals.grid.array_of_cells[76], globals.grid.array_of_cells[77]],
			 [globals.grid.array_of_cells[24],globals.grid.array_of_cells[25], globals.grid.array_of_cells[26], globals.grid.array_of_cells[51], globals.grid.array_of_cells[52], globals.grid.array_of_cells[53], globals.grid.array_of_cells[78], globals.grid.array_of_cells[79], globals.grid.array_of_cells[80]]
			 ]

globals.board = _board()
globals.grid._createsolution(globals.board)
globals.grid.generate_board(globals.board)

globals.grid.print_grid_array() #debug
while globals.running:
    # ----EVENT HANDLING--------------------------------------------------------
    for event in pygame.event.get():
        globals.curr_event = event
        
        if event.type == pygame.QUIT:
            globals.running = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                     globals.mute_flag = not globals.mute_flag
                     mute_music()
                if event.key == pygame.K_f:
                      globals.screen_info = not globals.screen_info
        # FOR WINDOW RESIZE
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
    


