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
from src.neo.config import WIDTH, HEIGHT, WHITE, BLACK, FPS
from src.neo import globals
from src.neo.gameState import gameStateManager
from src.neo.utils import resource_path

pygame.init()

# Set up display dimensions
globals.screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sudoku")

#----MUSIC--------------------------------------------------------------------
song = resource_path(os.path.join("assets/sounds", "flowers.mp3"))
mixer.music.load(song)

mixer.init() 
mixer.music.load(song) 
mixer.music.set_volume(0.7) 
mixer.music.play(-1, 0.0) 
#----INIT--------------------------------------------------------------------
clock = pygame.time.Clock()
globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', 30)


# Game loop--------------------------------------------------------------------
globals.running = True
globals.screen.fill(BLACK)  # Fill the background with black
game = gameStateManager()
game.run() #main menu
while globals.running:
    clock.tick(FPS)
    # ----EVENT HANDLING--------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.running = False
        
        game.get_input(event)
        game.run()
        pygame.display.flip


    #-----DRAWING--------------------------------------------------
    

    # -------------------------------------------------------------
    pygame.display.flip()

pygame.quit()
