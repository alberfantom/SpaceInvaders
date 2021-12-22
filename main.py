import pygame, sys

class Game:
    def __init__(self):
        pass

    def run(self):
        pass

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

