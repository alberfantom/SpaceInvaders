import pygame

from settings import *

class Obstacle(pygame.sprite.Group):
    class Block(pygame.sprite.Sprite):
        def __init__(self, start_x, start_y, size):
            super().__init__()
            
            self.start_x = start_x
            self.start_y = start_y

            self.size = size

            self.image = pygame.Surface((size, size))
            self.rect = self.image.get_rect(topleft=(self.start_x, self.start_y))

            self.image.fill((0, 0, 255))

    def __init__(self, shape, start_x, start_y):
        super().__init__()
        
        self.shape = shape

        self.width = len(self.shape[0]) * BLOCK_SIZE
        self.height = len(self.shape) * BLOCK_SIZE

        self.start_x = start_x
        self.start_y = start_y

    def fill(self, size_block):
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column == "*":
                    start_x = column_index * size_block + self.start_x
                    start_y = row_index * size_block + self.start_y
                    
                    block_sprite = self.Block(start_x, start_y, size_block)
                    self.add(block_sprite)