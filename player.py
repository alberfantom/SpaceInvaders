import pygame
import bullet

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, file_name, screen_width, screen_height):
        super().__init__()

        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(screen_width / 2, screen_height))

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = player_speed

        # Стрельба
        self.bullets = pygame.sprite.Group()

        self.is_ready = True
        self.cooldown = weapon_cooldown

    def update(self):
        keys = pygame.key.get_pressed()

        # Движение
        if self.rect.left >= 0:
            if keys[pygame.K_a]:
                self.rect.x -= self.speed

        if self.rect.right <= self.screen_width:
            if keys[pygame.K_d]:
                self.rect.x += self.speed

        # Стрельба
        if keys[pygame.K_SPACE]:
            if self.is_ready:
                self.shoot()
                self.is_ready = False
                self.time_when_shot = pygame.time.get_ticks()

            else:
                self.recharge()

    def shoot(self):
        bullet_sprite = bullet.Bullet("images\\bullet.png", self.rect.midtop, self.screen_height)
        self.bullets.add(bullet_sprite)

    def recharge(self):
            self.time_current = pygame.time.get_ticks()
            if self.time_current - self.time_when_shot >= self.cooldown:
                self.is_ready = True