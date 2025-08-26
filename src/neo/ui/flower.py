import pygame

class Flower(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("assets/art/flower/ff1_64.png"))
        self.sprites.append(pygame.image.load("assets/art/flower/ff2_64.png"))
        self.sprites.append(pygame.image.load("assets/art/flower/ff3_64.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]

    def animate(self):
        self.is_animating = True
    
    def update(self):
        # if self.is_animating:
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
        self.current_sprite += 0.05
        # print(int(self.current_sprite))
        # print(len(self.sprites))
    