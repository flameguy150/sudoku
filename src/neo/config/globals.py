# Screen variables
WIDTH= 600
HEIGHT = 600

#screen editing
screen = None
running = None # game loop variable
font_number_size = None

#custom fonts
custom_font = None
cf_small = None

# Game variables
grid = None
state = None


#Music
mute_flag = None

SUDOKU_DJ = None

#event
curr_event = None
screen_info = True

#controls
holding_num = 1

#settings
settings_on = False

#flower
flower = None

#grid
cell_grid = None
board = None

random_cells = None # this will be used to randomize board
init_flag = False #this to stop redrawing the beginning board everytime


# number of correctly filled cells
current_correct_cells = 0

#holds how many mistakes player made
mistakes = 0

# total time spent on game and time spent on the current puzzle
total_time = 0 # would have to access this through a txt file
current_time = 0 # would have to access this through a txt file