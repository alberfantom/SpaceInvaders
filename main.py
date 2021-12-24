import pygame, sys
import obstacle
import player

from settings import *

class Game:
    def __init__(self):
        player_sprite = player.Player(player_image, screen_width, screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.obstacle_0 = obstacle.Obstacle(shape, size_shape, 124, 350)

    def run(self):
        self.player.update()
        self.player.draw(screen)

        self.player.sprite.bullets.draw(screen)
        self.player.sprite.bullets.update()

        self.obstacle_0.draw(screen)
        self.obstacle_0.update()
        
if __name__ == "__main__":
    pygame.init()

    screen_width, screen_height = 1280, 720
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