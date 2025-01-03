# rect_info = [attribute1, a2, a3, ..., a4]

import pygame

screen = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('sudoku_util') 
background_colour = (234, 212, 252) 
screen.fill(background_colour) 

cells = []

hovered = False


pygame.font.init()


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
		cell_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width + 2, height + 2))
		cell = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		cells.append(cell)
		# self.info.rect = cell

	def draw_number(self):
		self.info.has_filled = True
		pass

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
		for i in range(4): #vertical lines
			self.xline = self.draw_line((0,0,0), 40 + 240*i, 40, 40 + 240*i, 760, 5)
		for x in range(4): #horizontal lines
			self.yline = self.draw_line((0,0,0), 40, 40 + 240*x, 760, 40+ 240*x, 5)

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

	def highlight(self):
		global hovered

		for cell in cells:
			# if cell.info.has_filled == False:
			# # do some highlighting
			# 	pass
			# else:
			# 	pass

			left = cell.left
			top = cell.top
			width = cell.width
			height = cell.height

			if event.type == pygame.MOUSEMOTION:
					
					if cell.collidepoint(pygame.mouse.get_pos()) and not hovered:
						left = cell.left
						top = cell.top
						width = cell.width
						height = cell.height

						
						outline = Cell.create_cell(screen, (0,0,0), left - 1, top - 1, width + 2, height + 2)
						highlight_lol = Cell.create_cell(screen, (255, 40, 0), left, top, width, height)
						hovered = True
					elif not cell.collidepoint(pygame.mouse.get_pos()): # draw white rectangle to replace red when cursor not over rectangle
						# highlight_lol = pygame.draw.rect(screen, color, pygame.Rect(rectangle[1]))
						Cell.create_cell(screen, (255,0,0), left, top, width, height)
						hovered = False
					elif not cell.collidepoint(pygame.mouse.get_pos()):
						hovered = False
	

				
				
				




# rect1 = rect_info(100, 100, False)
# rect2 = rect_info(200, 200, True)

# rect_info[3] = True   # They don't understand

# rect2.has_filled = True

# if (__name__ == "__main__"):
	
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

		
		grid = Grid(screen)
		grid.draw_grid()
		grid.highlight()


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