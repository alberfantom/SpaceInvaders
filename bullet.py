import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, file_name, position):
        super().__init__()

        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)

        self.speed = 12

    def update(self):
        self.rect.y -= self.speed