import pygame, sys
from player import Player

from settings import *

class WindowGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        player_sprite = Player(PLAYER_IMAGE, PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.background = None

    def load_background(self, file_path):
        self.screen_background = pygame.image.load(file_path)

        self.screen_background = pygame.transform.scale(self.screen_background, 
            (self.screen.get_width(), self.screen.get_height()))

        self.screen_background_rect = self.screen_background.get_rect(topleft=(0, 0))

    def events_handling(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                    sys.exit()

            if self.background:
                self.screen.blit(self.screen_background, self.screen_background_rect)
            
            else:
                self.screen.fill((BLACK))

            self.player.update()
            self.player.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    WindowGame().events_handling()