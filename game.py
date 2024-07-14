# libraries
import pygame, sys
from scripts.constant import *
from scripts.Entity import Bat, Ball

class Game:
    def __init__(self):

        # initialize pygame
        pygame.init()
        pygame.display.set_caption("Brick'N Ball")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_running = True

        # assets for game
        self.assets={
                "bat":(100,40),
                "ball":(30,30),
                "player":(WIDTH / 2, HEIGHT -50),
                "ball_speed": 300,
                "player_speed":400,
            }
        

        # sprites
        self.all_sprites = pygame.sprite.Group()
        self.bat_sprites = pygame.sprite.Group()
        self.player = Bat(self, (self.all_sprites, self.bat_sprites))
        self.ball = Ball(self, self.all_sprites, self.bat_sprites, self.player)

    def game_play(self):
        while self.game_running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.ball.launched:
                        self.ball.launch()
                        print("launched")   

            # update
            self.all_sprites.update(dt)
            # draw
            self.screen.fill(COLOR['bg'])
            self.all_sprites.draw(self.screen)
            #update game 
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.game_play()
