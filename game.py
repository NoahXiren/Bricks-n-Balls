# libraries
import pygame, sys
from scripts.constant import *
from scripts.Entity import Bat, Ball
from scripts.obstacle import Obstacle
from scripts.groups import Allsprite
import random

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
                "bat":(60,20),
                "ball":(20,20),
                "obstacle":(50,20),
                "player":(WIDTH / 2, HEIGHT -50),
                "ball_speed": 200,
                "player_speed":400,
            }
        

        # sprites
        self.all_sprites = Allsprite()
        self.bat_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.player = Bat(self, (self.all_sprites, self.bat_sprites))
        self.ball = Ball(self, self.all_sprites, self.bat_sprites, self.player, self.update_score)

        self.create_obstacles()

        # score
        self.score = {'player': 0}
        self.font = pygame.font.Font(None, 30)

    def create_obstacles(self):
        for i in range(10, 490, self.assets["obstacle"][0] + 10):
            for j in range(0, 250, self.assets["obstacle"][1] + 10):
                color = COLOR["obstacle_1"] if random.random() > 0.5 else COLOR["obstacle_2"]
                Obstacle(self, (self.all_sprites, self.obstacle_sprites), i, j, color)

    #score methods
    def display_score(self):
        # Render the score label text
        text_surf = self.font.render("Score: {}".format(self.score['player']), True, COLOR["text"])
        text_rect = text_surf.get_rect(midleft=(10, HEIGHT - 20))  
        self.screen.blit(text_surf, text_rect)
        
        # line separator
        pygame.draw.line(self.screen, COLOR["text"], (0, HEIGHT-40), (WIDTH, HEIGHT -40), 4)

    def update_score(self,side):
        self.score['player'] += 5
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
            # self.all_sprites.draw(self.screen)
            self.all_sprites.draw()
            self.display_score()


            #update game 
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.game_play()
