import pygame
from src.neo.config import globals
from src.neo.core.cell import Cell
from src.neo.config.constants import RED, TITLE_MENU_BG, GAME_BG, WHITE, BLACK, BLUE, GREEN


class Grid:
    '''Grid class to keep track of arrays'''
    def __init__(self):
        '''
        during self construction, init grid array so that we can track the array globally
        '''
        self.width = globals.WIDTH
        self.height = globals.HEIGHT
        
        self.array_of_cells = [] #holds all the cells

        self.init_grid_array() 
    
    def init_grid_array(self):
        '''
        to help visualize board
        to smoothe out corners, replace the code for horizontal grid lines with this:
        self.draw_line(BLACK, horizontal_offset - 2, vertical_offset + (x*(3*height)), globals.WIDTH - horizontal_offset, vertical_offset + (x*(3*height)), 5)   
        '''
        horizontal_offset = globals.WIDTH/8 #75 -- 450 -- 75 // 125 -- 750 -- 125
        vertical_offset = globals.HEIGHT/8 # 75- -- 450 -- 75 // 100 -- 600 -- 100

        width = globals.WIDTH/12
        height = globals.HEIGHT/12 # DEFAULT = 50 (600/12)

        cell_position_index = 0
        for column in range(9):
            for row in range(9):
                left = horizontal_offset + (column)*width
                top = vertical_offset + (row)*height

                cell = Cell(globals.screen, WHITE, left, top, width, height, cell_position_index)  
                self.array_of_cells.append(cell)
                cell_position_index += 1
    
    def resize_array(self):
        horizontal_offset = globals.WIDTH/8 #75 -- 450 -- 75 // 125 -- 750 -- 125
        vertical_offset = globals.HEIGHT/8 # 75- -- 450 -- 75 // 100 -- 600 -- 100

        width = globals.WIDTH/12
        height = globals.HEIGHT/12 # DEFAULT = 50 (600/12)

        for column in range(9):
            for row in range(9):
                index = row * 9 + column
                left = horizontal_offset + (column)*width
                top = vertical_offset + (row)*height
                #create white cells init
                new_rect = pygame.draw.rect(globals.screen, WHITE, pygame.Rect(left, top, width, height))

                self.array_of_cells[index].resize_cell(left, top, width, height, new_rect)

    def draw_9x9_board(self):
        for cell in self.array_of_cells:
            cell.draw_cell()

    def draw_line(self, the_color, x1, y1, x2, y2, width): 
        # need this to draw thicker lines between the 9 3x3 boxes
        line = pygame.draw.line(globals.screen, the_color, (x1,y1), (x2,y2), width)
        
    def draw_grid_outlines(self):
        '''
        to future me or someone else, why make a seperate function for the grid outlines? 
        so the highlight function doesn't draw over the grid and make the squares pop
        '''
        horizontal_offset = globals.WIDTH/8 #75 -- 450 -- 75 // 125 -- 750 -- 125
        vertical_offset = globals.HEIGHT/8 # 75- -- 450 -- 75 // 100 -- 600 -- 100

        width = globals.WIDTH/12
        height = globals.HEIGHT/12 # DEFAULT = 50 (600/12)

        for i in range(4): #vertical lines
            self.draw_line(BLACK, horizontal_offset + (i*(3*width)), vertical_offset, horizontal_offset + (i*(3*width)), globals.HEIGHT - vertical_offset, 5)
        for x in range(4): #horizontal lines
            self.draw_line(BLACK, horizontal_offset + 2, vertical_offset + (x*(3*height)), globals.WIDTH - horizontal_offset, vertical_offset + (x*(3*height)), 5)   

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

    def controls(self, event):
        pass
            

    # ---------- FOR DEBUGGING ------------------- ------------------- -------------------
    def get_mouse_pos(self):
        x,y = pygame.mouse.get_pos()
        print(f"x: {x}, y: {y}")
    
    def print_grid_array(self):
        i = 0
        for cell in self.array_of_cells:
            if i < 8:
                print(cell.position, end = " ")
                i += 1
            else:
                print(cell.position, end = " ")
                print()
                i = 0
    