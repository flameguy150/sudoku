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
from src.neo.utils.utilities import resource_path, mute_music

pygame.init()

# Icon
icon_image = pygame.image.load('assets/art/icon_256.png') 
pygame.display.set_icon(icon_image)

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
globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', 30)


# Game loop--------------------------------------------------------------------
globals.running = True
globals.screen.fill(BLACK)  # Fill the background with black
game = gameStateManager()
game.run() #main menu
globals.grid = Grid() #Init grid here

globals.grid.print_grid_array() #debug
while globals.running:
    clock.tick(FPS)
    # ----EVENT HANDLING--------------------------------------------------------
    for event in pygame.event.get():
        globals.curr_event = event
        
        if event.type == pygame.QUIT:
            globals.running = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                     globals.mute_flag = not globals.mute_flag
                     mute_music()
        # FOR WINDOW RESIZE
        elif event.type == pygame.VIDEORESIZE:
                # Update screen dimensions and recreate the display surface
                globals.WIDTH, globals.HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT), pygame.RESIZABLE)
                globals.grid.resize_array()
                pygame.display.flip()
                

        game.get_input(event)
        game.run() # this can display different screen
        pygame.display.flip()


    #-----DRAWING--------------------------------------------------
    

    # -------------------------------------------------------------
    pygame.display.flip()

pygame.quit()
