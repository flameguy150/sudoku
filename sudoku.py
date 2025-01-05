import pygame 
 



# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((800, 800)) 

# Set the caption of the screen 
pygame.display.set_caption('sudoku') 

# Fill the background colour to the screen 
screen.fill(background_colour) 

color = (255, 255, 255)

grid_rectangles = []

hovered = False
		
pygame.font.init()

number_holder = 0 #this will be the number that the user is holding, which can be printed out by left clicking

def mouse_print():
	if event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 1:
			print("Left mouse button clicked at:", event.pos)
			print(grid_rectangles[0][0])
			print(grid_rectangles[0][1])
		elif event.button == 3:
			print("Right mouse button clicked at:", event.pos)

		
def highlight():
	# highlight_spot = pygame.draw.Rect(screen, (105,150,230), pygame.draw.Rect())
	#if the mouse cursor hovers the rectangle, it will change 
	
	# for rectangle in grid_rectangles:
	# 	if position != rectangle:
	# 		pass
	# 	else:
	# 		highlight_lol = pygame.draw.rect(screen, (105,150,230), pygame.Rect(grid_rectangles[1]))
	# for rectangle in grid_rectangles:
	# 	if rectangle[0].collidepoint(position):
	# 		print("Mouse clicked on object!")
	global hovered
	# if grid_rectangles[0][0].collidepoint(pygame.mouse.get_pos()):
	# 	highlight_lol = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(grid_rectangles[0][1]))
	# 	print(highlight_lol)
	for rectangle in grid_rectangles:
		if event.type == pygame.MOUSEMOTION:
				if rectangle[0].collidepoint(pygame.mouse.get_pos()) and not hovered:
					left = rectangle[1][0]
					top = rectangle[1][1]
					width = rectangle[1][2]
					height = rectangle[1][3]

					
					outline = draw_rectangle((0,0,0), left - 1, top - 1, width + 2, height + 2)
					highlight_lol = pygame.draw.rect(screen, (255, 40, 0), pygame.Rect(rectangle[1]))
					hovered = True
				elif not rectangle[0].collidepoint(pygame.mouse.get_pos()): # draw white rectangle to replace red when cursor not over rectangle
					# highlight_lol = pygame.draw.rect(screen, color, pygame.Rect(rectangle[1]))
					draw_rectangle(color, rectangle[1][0], rectangle[1][1], rectangle[1][2], rectangle[1][3])
					hovered = False
				# elif not rectangle[0].collidepoint(pygame.mouse.get_pos()):
				# 	hovered = False

	

def create_grid():
	for i in range(9):
		for j in range(9):
			left_factor = 80 * j
			top_factor = 80 * i
			left = screen.get_width()-760 + left_factor
			top = screen.get_height()-760 + top_factor
			width = 80
			height = 80
			outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width+2, height+2))
			rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))

			index =  j + 9*i
			has_number = 0 #0 - not filled, 1 - has number, rectangle[3]
			
			rect_info = [rect, (left, top, width, height), index, has_number]
			
			grid_rectangles.append(rect_info)


			# Make a tuple (rect, (left_factor, top_factor, left, top))
			# Save that guy into a list
			# This is a very hacky way to save information, switch to a better way later
			
	# line = pygame.draw.rect(screen, color, pygame.Rect(30,30,30,30))
	#
	# NEED THIS LINE FOR REDRAWING WHITE RECTANGLE WHEN NOT HOVERING

def draw_grid():
	for i in range (3):
		for j in range(3):
			draw_3x3(i, j)

	#grid outlines
	for i in range(4): #vertical lines
		line = draw_line((0,0,0), 40 + 240*i, 40, 40 + 240*i, 760, 5)
	for x in range(4): #horizontal lines
		line = draw_line((0,0,0), 40, 40 + 240*x, 760, 40+ 240*x, 5)
	

def draw_3x3(x, y):
		for i in range (3):
			for j in range (3):
				left_factor = 80*j + (x*240)
				top_factor = 80*i + (y*240)
				color = (255, 255, 255)
				left = screen.get_width()-760 + left_factor
				top = screen.get_height()-760 + top_factor
				width = 80
				height = 80
				draw_rectangle(color, left, top, width, height)
				


def draw_rectangle(the_color, left, top, width, height):
	outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width+2, height+2))
	rect = pygame.draw.rect(screen, the_color, pygame.Rect(left, top, width, height))
	rect_info = [rect, (left, top, width, height)]
	# grid_rectangles.append(rect_info)
	

def draw_line(the_color, x1, y1, x2, y2, width): # need this to draw thicker lines between the 9 3x3 boxes
		line = pygame.draw.line(screen, the_color, (x1,y1), (x2,y2), width)

def create_grid_outlines():
	for i in range(4): #vertical lines
		line = draw_line((0,0,0), 40 + 240*i, 40, 40 + 240*i, 760, 5)
	for x in range(4): #horizontal lines
		line = draw_line((0,0,0), 40, 40 + 240*x, 760, 40+ 240*x, 5)

#

font = pygame.font.Font(None,36)


def numbers():#trying to see if i cant print numbers inside the boxes / need to eventually generate random numbers
	inc = 1
	counter = 0  #this will tell me where the numbers need to be placed
	print = 0 #ill have this to know what it needs to print
	for rectangle in grid_rectangles:
		counter = 0 #if counter is >3, counter
		if inc == 10:
			inc = 1
		text_surface = font.render(str(inc), True, (0,0,255))
		screen.blit(text_surface, rectangle[0])
		inc += 1

def fill_value(num): #function to input number in cell
	global hovered
	#this is gonna need mouse position to identify rectangle and see which cell to print number
	if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for rectangle in grid_rectangles:
					if rectangle[0].collidepoint(pygame.mouse.get_pos()):
							left = rectangle[1][0]
							top = rectangle[1][1]
							width = rectangle[1][2]
							height = rectangle[1][3]

							outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width+2, height+2))
							rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
							
							# use draw_rectangle for these 

							text_surface = font.render(str(num), True, (0,0,255))
							screen.blit(text_surface, rect)#replace rectangle with new white rectangle w number
							
							rectangle[3] = has_number = 1
							rect_info = [rect, (left, top, width, height), rectangle[2], has_number]
							# grid_rectangles.delete[rectangle]
							grid_rectangles[rectangle[2]] = rect_info #replace this empty cell with new cell tha thas number
							print("yep im printing")
		#we need an error detection when inputting wrong number
		



create_grid()


# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

# game loop 
while running: 
	
# for loop through the event queue 
	for event in pygame.event.get(): 
	
		# Check for QUIT event	 
		if event.type == pygame.QUIT: 
			running = False
		position = pygame.mouse.get_pos() 

		
		
		

		mouse_print()
		# highlight()
		highlight()
		fill_value(1)
		
		
		create_grid_outlines()
		
		# numbers()

		pygame.display.flip() 
		
			   



# In order to put anything on github, you want the following pattern
# git init once
# add ., commit, push