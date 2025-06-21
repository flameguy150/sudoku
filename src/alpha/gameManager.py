import pygame
import sys
from alpha.sudoku import Cell, Grid, mainloop
from alpha.sudoku_boards import easygrid1_, easygrid1_solution, is_valid, _board


FPS = 60
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,800))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)

        self.states = {'start':self.start, 'level':self.level}
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.gameStateManager.set_state('level')
                
                self.states[self.gameStateManager.get_state()].run()
                
                pygame.display.update()
                self.clock.tick(FPS)


class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        mainloop()


class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.fill('red')

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()