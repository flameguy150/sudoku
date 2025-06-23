import pygame
from src.neo import globals
from src.neo.config import RED, TITLE_MENU_BG, GAME_BG, WHITE, BLACK


class Grid:
    '''Grid class to keep track of arrays'''
    def __init__(self):
        self.width = globals.WIDTH
        self.height = globals.HEIGHT
    
    def draw_line(self, the_color, x1, y1, x2, y2, width): 
        # need this to draw thicker lines between the 9 3x3 boxes
        line = pygame.draw.line(globals.screen, the_color, (x1,y1), (x2,y2), width)
    
    def draw_9x9_example(self):
        '''to help visualize board'''
        horizontal_offset = globals.WIDTH//8 #75 -- 450 -- 75
        vertical_offset = globals.HEIGHT//8 # 75- -- 450 -- 75

        width = globals.WIDTH//12
        height = globals.HEIGHT//12 # DEFAULT = 50 (600/12)

        for column in range(9):
            for row in range(9):
                left = horizontal_offset + (column)*width
                top = vertical_offset + (row)*height
                cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(left - 1, top - 1, width + 2, height + 2))
                cell_rect = pygame.draw.rect(globals.screen, WHITE, pygame.Rect(left, top, width, height))  

        #grid outlines
        for i in range(4): #vertical lines
            self.draw_line(BLACK, horizontal_offset + (i*(3*width)), vertical_offset, horizontal_offset + (i*(3*width)), globals.HEIGHT - vertical_offset, 5)
        for x in range(4): #horizontal lines
            self.draw_line(BLACK, horizontal_offset, vertical_offset + (x*(3*height)), globals.WIDTH - horizontal_offset, vertical_offset + (x*(3*height)), 5)   

   

    def draw_3x3(self):
        '''Draw 3x3 grid, will use this later to make 9 3x3 cells'''
        horizontal_offset = 50
        vertical_offset = 25

        for column in range(3):
            for row in range(3):
                left = horizontal_offset * (column+1)
                top = vertical_offset * (row + 1)
                width = 50
                height = 25
                cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(left - 1, top - 1, width + 2, height + 2))
                cell_rect = pygame.draw.rect(globals.screen, WHITE, pygame.Rect(left, top, width, height))
    

class gameStateManager:
    def __init__(self):

        self.state = "menu"

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

    def run(self):
        if self.state == "menu":
            self.main_menu()
        elif self.state == "game":
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

        grid = Grid()

        grid.draw_9x9_example()

    
    def settings(self):
        pass





