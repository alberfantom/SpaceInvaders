import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, file_name, screen_width, screen_height):
        super().__init__()

        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(screen_width / 2, screen_height))

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = 6

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
            self.shoot()

    def shoot(self):
        pass