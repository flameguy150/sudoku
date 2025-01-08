# rect_info = [attribute1, a2, a3, ..., a4]

import pygame
from pygame import mixer


screen = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption('sudoku_util') 
background_colour = (234, 212, 252) 
screen.fill(background_colour) 

cells = []

input_num_print_list = [] #to delete off screen everytime input_num changes

hovered = False

# Starting the mixer 
mixer.init() 
  
# Loading the song 
mixer.music.load("RLbeat2.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0.7) 
  
# Start playing the song 
mixer.music.play(-1, 0.0) 

number_of_cells = 0 #keeping track if all 81 cells are in the cells list

input_num = 1 #the number that the player holds, so when they left click, that number will be drawn on cell
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
		self.filled = False
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
		self.filled = False
		self.is_red = False
		self.rect = 0
		self.number = 0 # the number drawn on cell
		self.correct_number = 0 #?might need it?

	# @staticmethod
	def create_cell(self, screen, color, left, top, width, height):
		global number_of_cells
		cell_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width + 2, height + 2))
		cell_rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		# cell = Cell(left, top, width, height)
		self.rect = cell_rect

		cells.append(self)
		
		# self.info.rect = cell
		number_of_cells += 1
	
	def change_cell(self, color = None, num = None): #change_cell(self, num), #change_cell
		global number_of_cells
		# delete cell
		# create new cell in red
		#cell.change_cell()
		# color = (255,0,0)

		#if cell.filled, do not change cell like AT ALL
		if self.filled:
			pass
		else:
			if color == None:
				color = (255,255,255)

			left = self.left 
			top = self.top 
			width = self.width 
			height = self.height 
			correct_num = self.correct_number
			
			index = cells.index(self)

			number_of_cells -= 1
			# self.create_cell(screen, color, left, top, width, height) #also known as the jiggly effect

			#create cell lol
			cell = Cell(left, top, width, height)
			cell_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left - 1, top - 1, width + 1, height + 1))
			cell_rect = pygame.draw.rect(screen, color, pygame.Rect(left, top, width - 1, height - 1))
			
			cell.rect = cell_rect
			cell.correct_number = correct_num
			# cell.rect.y = 10
			# cell.rect.right += 10

			# cells.append(cell) #TIME TO REPLACE
			
			
			if num == None:
				# don't font.render
				pass
			else:
				if num != cell.correct_number:
					print("wrong number inputted")
				else:
					text_surface = font.render(str(num), True, (0,0,255))
					cell.rect.left += 31
					cell.rect.top += 29
					screen.blit(text_surface, cell.rect)#replace rectangle with new white rectangle w number
					# cell.rect.left -= 2
					# cell.rect.top -= 2
					cell.filled = True
					cell.number = num
			# print(index)
			cells[index] = cell
			# self.info.rect = cell
			number_of_cells += 1

		
		


	# @classmethod
	def draw_number(self):
		global input_num
		if self.filled == True:
			pass # dont draw number
		else: 
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1: # left click on mouse
					# for cell in cells:
					if self.rect.collidepoint(pygame.mouse.get_pos()):
							# left = self.left
							# top = self.top
							# width = self.width
							# height = self.height

							self.change_cell(num = input_num) # after i change cell, the cell changes, so is self.filled being called on old cell or new cell?
							
							# text_surface = font.render(str(input_num), True, (0,0,255))
							# screen.blit(text_surface, rect)#replace rectangle with new white rectangle w number
							
							# cell.has_filled = has_number = True

							# print("yep im printing") #debugging tool YA FEEL ME
			#we need an error detection when inputting wrong number

	def mouse_print(self):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("Left mouse button clicked at:", event.pos)
				# print(grid_rectangles[0][0]) #cell.rect
				# print(grid_rectangles[0][1]) #cell.left, cell.top, cell.width, cell.height
			elif event.button == 3:
				print("Right mouse button clicked at:", event.pos)
	
	
	def highlight(self):
		global hovered

		# for cell in cells:
			# if cell.info.has_filled == False:
			# # do some highlighting
			# 	pass
			# else:
			# 	pass

			#self.filled, maybe highlight it a different, lighter color like blue or something

		if event.type == pygame.MOUSEMOTION:
				if self.rect.collidepoint(pygame.mouse.get_pos()):
					if self.filled:
						pass #DONT HIGHLIGHT
					else:
						self.change_cell(color = (255,0,0))# changes the cell to red
						hovered = True
					#issue, cell.create_cell is adding onto the number of cells in the cell list
					#instead of creating a new red cell, i should just change the color of the original cell into red when its hovered

					# outline = Cell.create_cell(screen, (0,0,0), left - 1, top - 1, width + 2, height + 2)
					# highlight_lol = Cell.create_cell(screen, (255, 40, 0), left, top, width, height)

				elif not self.rect.collidepoint(pygame.mouse.get_pos()): # draw white rectangle to replace red when cursor not over rectangle
					# highlight_lol = pygame.draw.rect(screen, color, pygame.Rect(rectangle[1]))
					color = (255, 255, 255)
					self.change_cell(color = color)
					hovered = False
				# elif not self.rect.collidepoint(pygame.mouse.get_pos()):
				# 	hovered = False

	def return_number(self): # lets see if the numbers are actually stored in the cell
		pass
		#for cell in cells:
		if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if self.rect.collidepoint(pygame.mouse.get_pos()):
						print(cell.number)




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
		# self.y2 = 
		for i in range (3):
			for j in range (3):
				left_factor = 80*j + (self.x*240)
				top_factor = 80*i + (self.y*240) # creates column of 3x3s first (top to bottom)
				color = (255, 255, 255)
				left = self.screen_width-760 + left_factor
				top = self.screen_height-760 + top_factor
				width = 80
				height = 80
				cell = Cell(left, top, width, height)
				cell.create_cell(screen, color, cell.left, cell.top, cell.width, cell.height)
				# cells.append(cell.info)


	def generate_grid(self):
		pass



	"""
		OTHER FUNCTIONS OF THE GAME
	"""
	def print_input_num(self, num): # make it so it deletes the previous input num and shows new one after changing number held
		# if num == 0:
		# 	white_ = font.render("", True, (0,0,255))
		# 	white_rect = (2, 2, 25, 25)
		# 	screen.blit(white_, white_rect)
		# else:
		# 	msg = "Currently inputing number " + str(num)
		# 	rect = (2, 2, 25, 25)
		# 	text_surface = font.render(msg, True, (0,0,255))
		# 	screen.blit(text_surface, rect)#replace rectangle with new white rectangle w number
		if len(input_num_print_list) == 0:
			msg = "Currently inputing number " + str(num)
			rect = pygame.draw.rect(screen, background_colour, pygame.Rect(2,2,350,25))
			text_surface = font.render(msg, True, (0,0,255))
			beginning_text = screen.blit(text_surface, rect)
			input_num_print_list.append(beginning_text)
		else: # need another elif statement for bc it keeps on print the same thing after the second print
			new_msg = "Currently inputing number " + str(num)
			rect = pygame.draw.rect(screen, background_colour, pygame.Rect(2,2,350,25))
			text_surface = font.render(new_msg, True, (0,0,255))
			text_on_screen = screen.blit(text_surface, rect)#replace rectangle with new white rectangle w number
			input_num_print_list[0] = text_on_screen
		"""
			OTHER FUNCTIONS OF THE GAME
		"""





		"""
		ALGO
		these should be activated once user inputs a number (pygame.KEYDOWN)
		"""

	def solution3(self): # check solution for each 3x3
		pass
	
	def solution9(self): # check if each row has all numbers by seeing if they add up to 45
		sum = 0 # see if sum == 45
		for i in range(9): #going through each row
			if sum != 45 or sum != 0:
				print("input is incorrect bro really? really now?")
			sum = 0 #reset sum after checking one row
			for j in range(9): # checking all elements in row
				index_ = (3 * j) + i
				sum += cells[index_].number # to access every cell, every cell should have indexes going 1-9 left to right, top to bottom, cells.index(cell)
	
	def solution_dup(self): #check for duplicates across 9x9
		pass


		
# list out of range bc cells has not been appended yet

				
				
#sudoku board?
#easy
easygrid1_ = [[0, 7, 0, 0, 2, 0, 0, 4, 6],
			  [0, 6, 0, 0 ,0 ,0, 8, 9, 0],
			  [2, 0, 0, 8, 0 ,0 ,7, 1, 5],
			  [0, 8, 4, 0, 9, 7, 0, 0, 0],
			  [7, 1, 0, 0, 0, 0, 0, 5, 9],
			  [0, 0, 0, 1, 3, 0, 4, 8, 0],
			  [6, 9, 7, 0, 0, 2, 0, 0, 8],
			  [0, 5, 8, 0, 0, 0, 0, 6, 0],
			  [4, 3, 0, 0, 8, 0, 0, 7, 0]
			  ]
easygrid1_solution = [[8, 7, 5, 9, 2, 1, 3, 4, 6],
		[3, 6, 1, 7, 5, 4, 8, 9, 2], 
		[2, 4, 9, 8, 6, 3, 7, 1, 5], 
		[5, 8, 4, 6, 9, 7, 1, 2, 3],
		[7, 1, 3, 2, 4, 8, 6, 5, 9],
		[9, 2, 6, 1, 3, 5, 4, 8, 7],
		[6 ,9, 7, 4, 1, 2, 5, 3, 8],
		[1, 5, 8, 3, 7, 9, 2, 6, 4],
		[4, 3, 2, 5, 8, 6, 9, 7, 1]
		]


#to generate a board, i just make it so that [1-9], randomly sort them out, if list[0][0] == list[1][0], that is NOT AUTHORIZED, so recreate list






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


cell_grid = [[cells[0] ,cells[1], cells[2], cells[27], cells[28], cells[29], cells[54], cells[55], cells[56]],
			 [cells[3], cells[4], cells[5], cells[30] ,cells[31], cells[32], cells[57], cells[58], cells[59]],
			 [cells[6], cells[7], cells[8], cells[33], cells[34], cells[35], cells[60], cells[61], cells[62]],
			 [cells[9], cells[10], cells[11], cells[36], cells[37], cells[38], cells[63 ], cells[64], cells[65]],
			 [cells[12],cells[13], cells[14], cells[39], cells[40], cells[41], cells[66], cells[67], cells[68]],
			 [cells[15],cells[16], cells[17], cells[42], cells[43], cells[44], cells[69], cells[70], cells[71]],
			 [cells[18],cells[19], cells[20], cells[45], cells[46], cells[47], cells[72], cells[73], cells[74]],
			 [cells[21],cells[22], cells[23], cells[48], cells[49], cells[50], cells[75], cells[76], cells[77]],
			 [cells[24],cells[25], cells[26], cells[51], cells[52], cells[53], cells[78], cells[79], cells[80]]
			 ]

for i in range (9): # go through every list, and sht
	for j in range(9):
		cell_grid[i][j].correct_number = easygrid1_[i][j]

cellular = Cell(80, 80, 80, 80)
grid.print_input_num(input_num)
# game loop 
while running: 
	
# for loop through the event queue 
	for event in pygame.event.get(): 

		""" CONTROLS"""

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
				running = False
			elif event.key == pygame.K_1:
				input_num = 1
			elif event.key == pygame.K_2:
				input_num = 2
			elif event.key == pygame.K_3:
				input_num = 3
			elif event.key == pygame.K_4:
				input_num = 4
			elif event.key == pygame.K_5:
				input_num = 5
			elif event.key == pygame.K_6:
				input_num = 6
			elif event.key == pygame.K_7:
				input_num = 7
			elif event.key == pygame.K_8:
				input_num = 8
			elif event.key == pygame.K_9:
				input_num = 9
			grid.print_input_num(input_num)

		""" CONTROLS"""

		# Check for QUIT event	(need this so that file can also be exited by pressing the red x on top right)
		if event.type == pygame.QUIT: 
			running = False

	
		for cell in cells:
			# cell.mouse_print()
			# print(number_of_cells)
			cell.draw_number()
			cell.highlight()
			cell.return_number() # yay its storing

		
		grid.create_grid_outlines()
		# for cell in cells:
		# 	cell.highlight()
		# if event.type == pygame.KEYDOWN:
		# 	grid.print_input_num(input_num) #maybe create a delete function to call before print?
		"""
		add cell.number to contain and access the number for each cell
		make sure in change_cell func that cell.number is changed
		add controls to change number that is held by user when they try to draw



		"""
		

		# numbers()

		pygame.display.flip() 
		
pygame.quit()
quit()



# In order to put anything on github, you want the following pattern
# git init once
# add ., commit, push
