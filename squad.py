import pygame

from settings import *

class Squad(pygame.sprite.Group):
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, file_path, start_x, start_y):
            super().__init__()

            self.image = pygame.image.load(file_path).convert_alpha()
            self.rect = self.image.get_rect(topleft=(start_x, start_y))

            self.start_x = start_x
            self.start_y = start_y

    def __init__(self, start_x, start_y):
        super().__init__()

        self.start_x = start_x
        self.start_y = start_y

    def fill(self, shape):
        for row_index, row in enumerate(shape):
            for column_index, column in enumerate(row):
                if column != " ":
                    start_x = column_index * 64 + self.start_x
                    start_y = row_index * 32 + self.start_y

                    enemy_image = SQUAD_IMAGES[int(shape[row_index][column_index])]
                    enemy_sprite = self.Enemy(enemy_image, start_x, start_y)
                    self.add(enemy_sprite)

                    print(start_x, start_y)