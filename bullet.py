import pygame

from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, file_name, position, screen_height):
        super().__init__()

        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)

        self.screen_height = screen_height

        self.speed = bullet_speed

    def update(self):
        if self.rect.bottom >= 0:
            self.rect.y -= self.speed
        
        else:
            self.kill()