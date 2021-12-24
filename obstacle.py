import pygame

from settings import *

class Obstacle(pygame.sprite.Group):
    def __init__(self, shape, size, x, y):
        super().__init__(self)

        self.shape = shape
        self.size = size

        self.obstacle_x = x
        self.obstacle_y = y

        self.blocks = str()

        self.__fill_obstacle()

    def __fill_obstacle(self):
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column == "x":
                    x = row_index * self.size + self.obstacle_y
                    y = column_index * self.size + self.obstacle_x
                
                    self.blocks += f"({y}, {x})\n"
                    self.add(Block(self.size, y, x))
    
    def __repr__(self):
        return self.blocks

class Block(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__() # <---

        self.size = size

        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.image.fill((255, 0, 0))

        self.x, self.y = x, y
    
    def update(self):
        pass 