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

        self.position = position

        self.number = 0 # hold the number within sudoku board
        self.filled = False # bool to see if correct number has already been inserted
    
    def draw_cell(self):
        cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(self.left - 1, self.top - 1, self.width + 2, self.height + 2))
        cell_rect = pygame.draw.rect(globals.screen, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
        self.rect = cell_rect
        self.draw_number()

    def highlight(self, event):
        '''
        another huge if statement
        basically, if mouse is hovered over cell that has not been filled with a number
        '''
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(pygame.mouse.get_pos()) and not self.filled:
                # print("highlighting!")
                self.change_cell(RED)

    def insert_number(self, event):
        '''
        function inserting number into sudoku board if cell is pressed

        ikr big if statement
        basically, if left click on mouse button is pressed down and cursor is hovered over cell
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.change_cell(WHITE, globals.holding_num)
    
    def draw_number(self):
        if self.number != 0: #dont draw empty cells
            text_surface = globals.custom_font.render(str(self.number), True, BLUE)
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