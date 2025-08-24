import pygame
from src.neo.config import globals
from src.neo.config.constants import RED, TITLE_MENU_BG, GAME_BG, WHITE, BLACK, BLUE, GREEN

'''
------------------------   GAME STATE MANAGER  ------------------------   ------------------------   ------------------------   
'''

class gameStateManager:
    def __init__(self):

        self.state = "menu"

        self.event = None

    def get_input(self, event):
        '''pass in input to see where to go'''

        #if in main menu
        if self.state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
                    globals.running = False

                #if main menu and press play
                elif event.key == pygame.K_p:
                    self.state = "game"

        #if in game
        if self.state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = "menu"
                else:
                    keymap = {
                        pygame.K_1: 1,
                        pygame.K_2: 2,
                        pygame.K_3: 3,
                        pygame.K_4: 4,
                        pygame.K_5: 5,
                        pygame.K_6: 6,
                        pygame.K_7: 7,
                        pygame.K_8: 8,
                        pygame.K_9: 9
                    }
                    if event.key in keymap:
                        globals.holding_num = keymap[event.key]

    def run(self):
        if self.state == "menu":
            # Menu_Level()
            self.main_menu()
        elif self.state == "game":
            # Game_Level(self.event)
            self.in_game_screen()
    
    def main_menu(self):
        globals.screen.fill(TITLE_MENU_BG)

        
        # texts
        custom_text = globals.custom_font.render("Welcome to Sudoku!", True, (140, 37, 150)) # Green text
        MSG = globals.custom_font.render("Press p to play", True, (100, 137, 150)) # Green text
        # draw text
        globals.screen.blit(custom_text, (globals.WIDTH // 2 - custom_text.get_width() // 2, 100)) # Center the text horizontally
        globals.screen.blit(MSG, (globals.WIDTH // 2 - MSG.get_width() // 2, 200)) # Center the text horizontally
        

    def in_game_screen(self):
        globals.screen.fill(GAME_BG)

        globals.grid.draw_9x9_board()

        # grid.get_mouse_pos()

        for cell in globals.grid.array_of_cells:
            cell.highlight(globals.curr_event)
            cell.insert_number(globals.curr_event)
            
        
        globals.grid.draw_grid_outlines() 


    def settings(self):
        pass





