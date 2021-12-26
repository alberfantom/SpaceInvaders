import pygame

class Weapon:
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, file_path):
            super().__init__()

            self.image = pygame.image.load(file_path).convert_alpha()
            self.rect = self.image.get_rect()

    def __init__(self, cooldown, start_x, start_y):
        self.cooldown = cooldown

    def shoot(self):
        pass