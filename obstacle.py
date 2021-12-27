import pygame

from settings import *

class Obstacle(pygame.sprite.Group):
    class Block(pygame.sprite.Sprite):
        def __init__(self, file_path, *position):
            super().__init__()

            self.image = pygame.image.load(file_path).convert_alpha()
            self.rect = self.image.get_rect(topleft=position)

    def __init__(self, shape, start_x, start_y):
        super().__init__()

        self.shape = shape
        
        self.start_x = start_x
        self.start_y = start_y

    def create_obstacles(self):
        self.obstacles = list()
        self.amount = None

        for _ in range(self.amount):
            self.obstacles.append()

    def fill_obstacle(self, block_image, block_size):
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                x_block = row_index * block_size
                y_block = column_index * block_size

                # Добавить в параметры BLOCK_IMAGE
                self.add(self.Block(block_image, x_block, y_block))

obstacle = Obstacle(OBSTACLE_SHAPE, OBSTACLE_START_X, OBSTACLE_START_Y)

obstacle.fill_obstacle(BLOCK_IMAGE, BLOCK_SIZE)

print(obstacle.sprites())