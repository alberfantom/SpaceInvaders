import pygame, sys

from player import Player
from obstacle import Obstacle
from squad import Squad

from settings import *

class WindowGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.player_sprite = Player(PLAYER_IMAGE, PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)

        self.weapon_sprite = self.player_sprite.weapon
        self.weapon = pygame.sprite.GroupSingle(self.weapon_sprite)

        self.obstacles = self.create_obstacles(OFFSET_BETWEEN_OBSTACLES, OBSTACLE_START_X, OBSTACLE_START_Y)

        self.enemies = Squad(SQUAD_START_X, SQUAD_START_Y)
        self.enemies.fill(SQUAD_SHAPE)

        self.background = None

    def load_background(self, file_path):
        self.screen_background = pygame.image.load(file_path)

        self.screen_background = pygame.transform.scale(self.screen_background, 
            (self.screen.get_width(), self.screen.get_height()))

        self.screen_background_rect = self.screen_background.get_rect(topleft=(0, 0))

    @staticmethod
    def create_obstacles(offset_between_obstacles, start_x, start_y):
        obstacles = list()
        amount = SCREEN_WIDTH // (OBSTACLE_WIDTH + offset_between_obstacles)
        
        if amount != 0:
            obstacle = Obstacle(OBSTACLE_SHAPE, start_x, start_y)
            obstacles.append(obstacle)
            obstacles[-1].fill(BLOCK_SIZE)

            for _ in range(amount - 1):
                obstacle = Obstacle(OBSTACLE_SHAPE, obstacles[-1].start_x + obstacles[-1].width + offset_between_obstacles, start_y)
                obstacles.append(obstacle)
                obstacles[-1].fill(BLOCK_SIZE)

        return obstacles

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

            self.weapon.update()
            self.weapon.draw(self.screen)

            self.weapon_sprite.bullets.update()
            self.weapon_sprite.bullets.draw(self.screen)

            for obstacle in self.obstacles:
                obstacle.update()
                obstacle.draw(self.screen)

            self.enemies.update()
            self.enemies.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    WindowGame().events_handling()