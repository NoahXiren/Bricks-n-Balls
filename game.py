# libraries
import pygame, sys
from scripts.constant import *


class Game:
    def __init__(self):

        # initialize pygame
        pygame.init()
        pygame.display.set_caption("Brick'N Ball")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_running = True

        # sprites
        self.sprites = pygame.sprite.Group()


    def game_play(self):
        while self.game_running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    pygame.quit()
                    sys.exit()

                # draw
            self.screen.fill(COLOR['screen'])
                #update game 
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.game_play()
