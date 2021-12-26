import pygame

from settings import *

class Weapon(pygame.sprite.Sprite):
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, file_path, position, speed):
            super().__init__()
            self.image = pygame.image.load(file_path).convert_alpha()
            self.rect = self.image.get_rect(midbottom=(position))
            self.speed = speed

        def update(self):
            if self.rect.bottom >= 0:
                self.rect.y -= self.speed

            else:
                self.kill()

    def __init__(self, file_path, cooldown, object, start_position):
        super().__init__()
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(start_position))
        self.object = object
        self.cooldown = cooldown
        self.bullets = pygame.sprite.Group()
        self.is_ready = True

    def update(self):
        self.object.movement(self.rect)

    def shoot(self):
        if self.is_ready:
            self.time_shooted = pygame.time.get_ticks()
            self.bullet_sprite = self.Bullet(BULLET_IMAGE, self.rect.center, BULLET_SPEED)
            self.bullets.add(self.bullet_sprite)
            self.is_ready = False
        else:
            self.recharge()

    def recharge(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.time_shooted >= self.cooldown:
            self.is_ready = True