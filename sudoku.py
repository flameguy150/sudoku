import pygame 


# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((800, 600)) 

# Set the caption of the screen 
pygame.display.set_caption('sudoku') 

# Fill the background colour to the screen 
screen.fill(background_colour) 

color = (255, 255, 255)

grid_rectangles = []

hovered = False
		


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
					print("Mouse clicked on object!")
					highlight_lol = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(rectangle[1]))
					hovered = True
				elif not rectangle[0].collidepoint(pygame.mouse.get_pos()) and hovered:
					# highlight_lol = pygame.draw.rect(screen, color, pygame.Rect(rectangle[1]))
					draw_rectangle(color, rectangle[1][0], rectangle[1][1], rectangle[1][2], rectangle[1][3])
					hovered = False
				elif not rectangle[0].collidepoint(pygame.mouse.get_pos()):
					hovered = False

	

def create_grid():
	for i in range(9):
		for j in range(9):
			left_factor = 80 * j
			top_factor = 50 * i
			left = screen.get_width()-760 + left_factor
			top = screen.get_height()-525 + top_factor
			width = 80
			height = 50
			outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width+2, height+2))
			rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
			rect_info = (rect, (left, top, width, height))
			grid_rectangles.append(rect_info)



			# Make a tuple (rect, (left_factor, top_factor, left, top))
			# Save that guy into a list
			# This is a very hacky way to save information, switch to a better way later
			
	# line = pygame.draw.rect(screen, color, pygame.Rect(30,30,30,30))
	#
	# NEED THIS LINE FOR REDRAWING WHITE RECTANGLE WHEN NOT HOVERING
	
def draw_rectangle(the_color, left, top, width, height):
	outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width+2, height+2))
	rect = pygame.draw.rect(screen, the_color, pygame.Rect(left, top, width, height))
	rect_info = (rect, (left, top, width, height))
	# grid_rectangles.append(rect_info)


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
		highlight()
		pygame.display.flip() 
		
			   

