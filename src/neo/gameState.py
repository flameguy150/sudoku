import pygame
from src.neo import globals
from src.neo.config import RED, TITLE_MENU_BG, GAME_BG, WHITE, BLACK, BLUE, GREEN


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

        
    def create_cell(self, color):
        '''
        cell outline should be -1 if 600x600
        '''
        
    
    def draw_cell(self):
        cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(self.left - 1, self.top - 1, self.width + 2, self.height + 2))
        cell_rect = pygame.draw.rect(globals.screen, self.color, pygame.Rect(self.left, self.top, self.width, self.height))
        self.rect = cell_rect
        self.draw_number()

    def highlight(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                # print("highlighting!")
                self.change_cell(RED)

    def insert_number(self, event):
        '''
        function inserting number into sudoku board if cell is pressed

        ikr big if statement
        basically, if left click on mouse button is pressed down and cursor is hovered over cell
        '''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.change_cell(BLUE, num = 1)
    
    def draw_number(self):
        if self.number != 0: #dont draw empty cells
            text_surface = globals.custom_font.render(str(self.number), True, GREEN)
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
                # cell_outline = pygame.draw.rect(globals.screen, BLACK, pygame.Rect(left - 1, top - 1, width + 2, height + 2))
                # cell_rect = pygame.draw.rect(globals.screen, WHITE, pygame.Rect(left, top, width, height))
                #create white cells init
                cell = Cell(globals.screen, WHITE, left, top, width, height, cell_position_index)  
                self.array_of_cells.append(cell)
                cell_position_index += 1
    
    def draw_9x9_example(self):
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

        globals.grid.draw_9x9_example()
        globals.grid.print_grid_array()

        # grid.get_mouse_pos()

        for cell in globals.grid.array_of_cells:
            cell.highlight(globals.curr_event)
            cell.insert_number(globals.curr_event)
        
        globals.grid.draw_grid_outlines() 


    def settings(self):
        pass





