import pygame
from src.neo.config import globals
from src.neo.config.constants import RED, TITLE_MENU_BG, GAME_BG, WHITE, BLACK, BLUE, GREEN


class Cell:
    def __init__(self, screen, color, left, top, width, height, position = None):
        '''
        coordinates to draw rectangle
        color for initial drawing
        self.rect for collision
        self.number holds the number inputted into cell
        '''
        self.screen = screen

        self.color = color

        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.rect = None #pygame rectangle object used for collision detection

        self.position = position # positional number in array

        self.number = 0 # hold the number drawn within sudoku board
        self.filled = False # bool to see if correct number has already been inserted

        self.correct_number = 0 # the correct number

    def init_rect(self):
        '''
        This function exists so I can init rects for the cells, this is neccesary because we must generate the solution and board before actually running the game through game loop.

        It is used when creating cells in grid.py. 
        I could probably just call it during the initialization of the cell but I'm too lazy and it seems minuscule
        '''
        cell_rect = pygame.draw.rect(globals.screen, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
        self.rect = cell_rect

    def draw_cell_init9x9(self):
        """
        This function exists so that when the initial board is drawn, the if statements in the bottom do not bother the rest of the drawing functions
        """
        cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(self.left - 1, self.top - 1, self.width + 2, self.height + 2))
        cell_rect = pygame.draw.rect(globals.screen, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
        self.rect = cell_rect
        
        if self.position not in globals.random_cells:
            self.draw_number()
        else:
            self.number = 0
            self.filled = False
        # ---------------------------------------------------------------------------
    
    def draw_cell(self):
        cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(self.left - 1, self.top - 1, self.width + 2, self.height + 2))
        cell_rect = pygame.draw.rect(globals.screen, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
        self.rect = cell_rect
        
        self.draw_number()
        # ---------------------------------------------------------------------------

    def highlight(self, event):
        '''
        another huge if statement
        basically, if mouse is hovered over cell that has not been filled with a number
        AND now if player is not in hud overlay, prevents them from playing while in settings. Might change honestly, not the worst feature
        '''
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(pygame.mouse.get_pos()) and globals.settings_on == False:
                # print("highlighting!")
            if self.filled == False:
                self.change_cell(RED)
            else: 
                pass

    def insert_number(self, event):
        '''
        function inserting number into sudoku board if cell is pressed

        ikr big if statement
        basically, if left click on mouse button is pressed down and cursor is hovered over cell
        AND now if player is not in hud overlay, prevents them from playing while in settings. Might change honestly, not the worst feature
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(pygame.mouse.get_pos()) and globals.settings_on == False:
            if self.filled:
                print("cell already filled")
            elif globals.holding_num != self.correct_number:
                print("incorrect!")
                globals.mistakes += 1
                print(globals.mistakes)
            else:
                self.change_cell(WHITE, globals.holding_num)
                print("correct!")
    

    def draw_number(self):
        if self.number != 0: #dont draw empty cells
            text_surface = globals.custom_font.render(str(self.number), True, BLUE)

            # middle of the cell depending on window size
            self.rect.left += 4
            self.rect.top += 5

            globals.screen.blit(text_surface, self.rect)#replace rectangle with new white rectangle w number
            self.filled = True

            
            
    def change_cell(self, color, num = 0):
        '''
        redraw rectangle with same coordinates of current cell
        '''
        cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(self.left - 1, self.top - 1, self.width + 1, self.height + 1))
        cell_rect = pygame.draw.rect(globals.screen, color, pygame.Rect(self.left, self.top, self.width-1, self.height-1))


        # for number input
        if num != 0:
            self.number = num
            self.draw_number()
    
    def resize_cell(self, left, top, width, height, rect):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = rect

    