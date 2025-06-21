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
from src.neo.config import WIDTH, HEIGHT, WHITE, BLACK
from src.neo import globals
from src.neo.gameState import main_menu

pygame.init()

# Set up display dimensions
globals.screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sudoku")

# Game loop
running = True
while running:
    # ----EVENT HANDLING--------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
                running = False
        if event.type == pygame.QUIT:
            running = False


    #-----DRAWING--------------------------------------------------
    # screen.fill(BLACK)  # Fill the background with black
    main_menu()

    # -------------------------------------------------------------
    pygame.display.flip()

pygame.quit()
