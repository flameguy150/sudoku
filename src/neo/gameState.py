import pygame
from src.neo import globals
from src.neo.config import RED, TITLE_MENU_BG, WIDTH, HEIGHT


class gameStateManager:
    def __init__(self):
        self.in_main_menu = True #initially true since we start with main menu
        self.in_game = False
        self.in_settings = False

    def get_input(self, event):
        '''pass in input to see where to go'''

        #if in main menu
        if self.in_main_menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
                    globals.running = False

                #if main menu and press play
                elif event.key == pygame.K_p:
                    self. in_main_menu = False
                    self.in_game = True

        #if in game
        if self.in_game:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.in_game = False
                    self. in_main_menu = True

    def run(self):
        if self.in_main_menu:
            self.main_menu()
        elif self.in_game:
            self.in_game_screen()

    def main_menu(self):
        globals.screen.fill(TITLE_MENU_BG)

        # draw text
        custom_text = globals.custom_font.render("Welcome to Sudoku!", True, (100, 137, 150)) # Green text
        globals.screen.blit(custom_text, (WIDTH // 2 - custom_text.get_width() // 2, 100)) # Center the text horizontally

    def in_game_screen(self):
        globals.screen.fill(RED)
    
    def settings(self):
        pass