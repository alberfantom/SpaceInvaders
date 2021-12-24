import pygame, sys
import player

from settings import *

class Game:
    def __init__(self):
        player_sprite = player.Player(player_image, screen_width, screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)

        self.player.sprite.bullets.draw(screen)
        self.player.sprite.bullets.update()

        print(self.player.sprite.bullets)
        
if __name__ == "__main__":
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    fps = 60
    clock = pygame.time.Clock()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                sys.exit()
        
        game.run()

        pygame.display.update()
        clock.tick(fps)

        screen.fill((0, 0, 0))