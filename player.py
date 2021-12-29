import pygame

from weapon import Weapon

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, file_path, start_x, start_y, speed):
        super().__init__()

        self.file_path = file_path

        self.image = pygame.image.load(self.file_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(start_x, start_y))

        self.speed = speed

        self.weapon = Weapon(WEAPON_IMAGE, WEAPON_COOLDOWN, self, self.rect.center)

    def update(self):
        self.movement(self.rect)

    def movement(self, object_rect):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if object_rect.left >= 0:
                object_rect.x -= self.speed

        if keys[pygame.K_d]:
            if object_rect.right <= SCREEN_WIDTH:
                object_rect.x += self.speed

        if keys[pygame.K_SPACE]:
            self.weapon.shoot()    