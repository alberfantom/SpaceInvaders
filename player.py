import pygame
from weapon import Weapon

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, file_path, start_x, start_y, speed):
        super().__init__()

        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(start_x, start_y))

        self.speed = speed

        self.weapon = Weapon(WEAPON_COOLDOWN)

    def update(self):
        self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed

        if keys[pygame.K_d]:
            if self.rect.right <= SCREEN_WIDTH:
                self.rect.x += self.speed

        if keys[pygame.SPACE]:
            self.weapon.shoot()

        