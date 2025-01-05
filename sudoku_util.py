# rect_info = [attribute1, a2, a3, ..., a4]

import pygame

screen = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('sudoku_util') 
background_colour = (234, 212, 252) 
screen.fill(background_colour) 

cells = []

hovered = False



number_of_cells = 0 #keeping track if all 81 cells are in the cells list

input_num = 0 #the number that the player holds, so when they left click, that number will be drawn on cell
#i will put controls down to switch number 1-9

pygame.font.init()
font = pygame.font.Font(None,36)

class rect_info:
	def __init__(self, Cell, left, top, width, height): #index? we shall see
		self.cell = Cell
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		# self.index = index
		self.has_filled = False
		self.rect = 0 #the actual pygame rectangle
	

#we need to append an actual Cell into cells so we can access highlight function
#

class Cell:
	def __init__(self, left, top, width, height):
		# self.info = rect_info(left, top, width, height)
		self.info = rect_info(self, left, top, width, height)
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		# self.index = index
		self.has_filled = False
		self.rect = 0

	@staticmethod
	def create_cell(screen, color, left, top, width, height):
		global number_of_cells
		cell_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width + 2, height + 2))
		cell_rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		cell = Cell(left, top, width, height)
		cell.rect = cell_rect
		cells.append(cell)
		# self.info.rect = cell
		number_of_cells += 1
	
	def change_cell(self, color = None, num = None): #change_cell(self, num), #change_cell
		global number_of_cells
		# delete cell
		# create new cell in red
		#cell.change_cell()
		# color = (255,0,0)
		if color == None:
			color = (255,255,255)
		left = self.left
		top = self.top
		width = self.width
		height = self.height
		
		index = cells.index(self)

		number_of_cells -= 1
		# self.create_cell(screen, color, left, top, width, height) #also known as the jiggly effect

		#create cell lol
		cell_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width + 2, height + 2))
		cell_rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		cell = Cell(left, top, width, height)
		cell.rect = cell_rect
		# cells.append(cell) #TIME TO REPLACE
		print(index)
		cells[index] = cell
		# self.info.rect = cell
		number_of_cells += 1

		text_surface = font.render(str(num), True, (0,0,255))
		screen.blit(text_surface, cell_rect)#replace rectangle with new white rectangle w number
		


	# @classmethod
	def draw_number(self):
		if self.info.has_filled == True:
			pass
			
		else:
			pass
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: # left click on mouse
				for cell in cells:
					if cell.rect.collidepoint(pygame.mouse.get_pos()):
							left = cell.left
							top = cell.top
							width = cell.width
							height = cell.height


							# rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
							# outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width+2, height+2))
							# use draw_rectangle for these 
							

							#create_cell() - need to access the rectangle of this new cell, how? - nvm
							#we are gonna make change cell also change num?
							cell.change_cell(num = 0)

							# text_surface = font.render(str(input_num), True, (0,0,255))
							# screen.blit(text_surface, rect)#replace rectangle with new white rectangle w number
							
							cell.has_filled = has_number = True
							# rect_info = [rect, (left, top, width, height), rectangle[2], has_number]
							# grid_rectangles.delete[rectangle]
							# grid_rectangles[rectangle[2]] = rect_info #replace this empty cell with new cell tha thas number
							print("yep im printing")
		#we need an error detection when inputting wrong number

	def mouse_print(self):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("Left mouse button clicked at:", event.pos)
				# print(grid_rectangles[0][0]) #cell.rect
				# print(grid_rectangles[0][1]) #cell.left, cell.top, cell.width, cell.height
			elif event.button == 3:
				print("Right mouse button clicked at:", event.pos)
	

	#Ig this function needs to be outside of the class bc i cant use it within another function in the same class
	# def draw_cell(self, screen, color, left, top, width, height):
	# 	cell_outline = pygame.draw.rect(screen, (0,0,0), pygame.rect(left, top, width, height))
	# 	cell = pygame.draw.rect(screen, color, pygame.rect(left, top, width, height))
	# 	cells.append(cell)

	# def highlight(self):
	# 	if self.info.has_filled == False:
	# 		# do some highlighting
	# 		pass
	# 	else:
	# 		pass

	# 	global hovered

	# 	for cell in cells:
	# 		if event.type == pygame.MOUSEMOTION:
	# 				if self.collidepoint(pygame.mouse.get_pos()) and not hovered:
	# 					left = cell.left
	# 					top = cell.top
	# 					width = cell.width
	# 					height = height

						
	# 					outline = Cell.create_cell(screen, (0,0,0), left - 1, top - 1, width + 2, height + 2)
	# 					highlight_lol = pygame.draw.rect(screen, (255, 40, 0), pygame.Rect())
	# 					hovered = True
	# 				elif not self.collidepoint(pygame.mouse.get_pos()): # draw white rectangle to replace red when cursor not over rectangle
	# 					# highlight_lol = pygame.draw.rect(screen, color, pygame.Rect(rectangle[1]))
	# 					Cell.create_cell(screen, (255,0,0), self.left, self.top, self.width, self.height)
	# 					hovered = False
	# 				elif not self.collidepoint(pygame.mouse.get_pos()):
	# 					hovered = False
	def highlight(self):
		global hovered

		# for cell in cells:
			# if cell.info.has_filled == False:
			# # do some highlighting
			# 	pass
			# else:
			# 	pass

		left = self.left
		top = self.top
		width = self.width
		height = self.height

		if event.type == pygame.MOUSEMOTION:
				
				if self.rect.collidepoint(pygame.mouse.get_pos()) and not hovered:
					left = self.left
					top = self.top
					width = self.width
					height = self.height

					#issue, cell.create_cell is adding onto the number of cells in the cell list
					#instead of creating a new red cell, i should just change the color of the original cell into red when its hovered





					# outline = Cell.create_cell(screen, (0,0,0), left - 1, top - 1, width + 2, height + 2)
					# highlight_lol = Cell.create_cell(screen, (255, 40, 0), left, top, width, height)
					self.change_cell(color = (255,0,0))# changes the cell to red
					hovered = True
				elif not self.rect.collidepoint(pygame.mouse.get_pos()): # draw white rectangle to replace red when cursor not over rectangle
					# highlight_lol = pygame.draw.rect(screen, color, pygame.Rect(rectangle[1]))
					color = (255, 255, 255)
					self.change_cell(color = color)
					hovered = False
				# elif not self.rect.collidepoint(pygame.mouse.get_pos()):
				# 	hovered = False

	











class Grid:
	def __init__(self, screen):
		# self.width_factor = width_factor
		# self.height_factor = height_factor
		self.screen_width = screen.get_width()
		self.screen_height = screen.get_height()

		self.xline = 0
		self.yline = 0

		self.x3 = 0

		self.x = 0
		self.y = 0
		
	def draw_line(self, the_color, x1, y1, x2, y2, width): # need this to draw thicker lines between the 9 3x3 boxes
		line = pygame.draw.line(screen, the_color, (x1,y1), (x2,y2), width)

	def create_grid_outlines(self):
		for i in range(4): #vertical lines
			line = self.draw_line((0,0,0), 40 + 240*i, 40, 40 + 240*i, 760, 5)
		for x in range(4): #horizontal lines
			line = self.draw_line((0,0,0), 40, 40 + 240*x, 760, 40+ 240*x, 5)

	def draw_grid(self):
		# Make 9 3x3 squares 
        # For each of these squares 
        # Each one is a Cell()
		for x in range(3):
			for y in range(3):
				self.x = x
				self.y = y
				self.draw_3x3()
		#grid outlines
		# for i in range(4): #vertical lines
		# 	self.xline = self.draw_line((0,0,0), 40 + 240*i, 40, 40 + 240*i, 760, 5)
		# for x in range(4): #horizontal lines
		# 	self.yline = self.draw_line((0,0,0), 40, 40 + 240*x, 760, 40+ 240*x, 5)

	def draw_3x3(self):
		# self.x2 = x
		# self.y2 = y
		for i in range (3):
			for j in range (3):
				left_factor = 80*j + (self.x*240)
				top_factor = 80*i + (self.y*240)
				color = (255, 255, 255)
				left = self.screen_width-760 + left_factor
				top = self.screen_height-760 + top_factor
				width = 80
				height = 80
				cell = Cell(left, top, width, height)
				cell.create_cell(screen, color, left, top, width, height)
				# cells.append(cell.info)
	def mouse_print(self):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("Left mouse button clicked at:", event.pos)
				# print(grid_rectangles[0][0]) #cell.rect
				# print(grid_rectangles[0][1]) #cell.left, cell.top, cell.width, cell.height
			elif event.button == 3:
				print("Right mouse button clicked at:", event.pos)
	
	

	


				
				
				




# rect1 = rect_info(100, 100, False)
# rect2 = rect_info(200, 200, True)

# rect_info[3] = True   # They don't understand

# rect2.has_filled = True

# if (__name__ == "__main__"):
	
# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

grid = Grid(screen)
grid.draw_grid()

cellular = Cell(80, 80, 80, 80)

# game loop 
while running: 
	
# for loop through the event queue 
	for event in pygame.event.get(): 
	
		# Check for QUIT event	 
		if event.type == pygame.QUIT: 
			running = False
		# grid.mouse_print()
		for cell in cells:
			# cell.mouse_print()
			# print(number_of_cells)
			cell.highlight()

		
		grid.create_grid_outlines()
		# for cell in cells:
		# 	cell.highlight()


		#'pygame.rect.Rect' object has no attribute 'highlight'

		# mouse_print()
		# highlight()
		
		# fill_value(1)
		# highlight()
		
		
		
		# numbers()

		pygame.display.flip() 
		
			   



# In order to put anything on github, you want the following pattern
# git init once
# add ., commit, push