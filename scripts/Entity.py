import pygame
from .constant import *

class Bat(pygame.sprite.Sprite):
    def __init__(self, game, groups):
        super().__init__(groups)
        self.game = game
        self.image = pygame.Surface(self.game.assets['bat'], pygame.SRCALPHA)
        # self.image.fill(COLOR['bat'])
        pygame.draw.rect(self.image,
                         COLOR["bat"],
                         pygame.FRect((0,0), self.game.assets['bat']),
                         0,5) #width and radius
        

        # rect and movements
        self.rect = self.image.get_frect(center = self.game.assets["player"])
        self.direction = 0
        self.speed = self.game.assets["player_speed"]
        self.old_rect = self.rect.copy()
    
    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    def move(self, dt):
        self.rect.centerx += self.direction * self.speed * dt
        
        # keep bat screen bounded horizontally
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def update(self,dt):
        self.get_direction()
        self.move(dt)

    def get_center(self):
        return self.rect.centerx, self.rect.top


class Ball(pygame.sprite.Sprite):
    def __init__(self, game, groups ,bat_sprites, bat):
        super().__init__(groups)
        self.bat_sprites = bat_sprites
        self.game = game
        self.bat = bat
        self.image = pygame.Surface(self.game.assets['ball'], pygame.SRCALPHA)
        # self.image.fill(COLOR['ball'])
        pygame.draw.circle(self.image,
                         COLOR["ball"],
                         (self.game.assets['ball'][0] / 2, # center_x
                          self.game.assets['ball'][1] / 2), # center_y
                          self.game.assets['ball'][0] / 2), # radius
        
        # rect and movements
        self.rect = self.image.get_frect()
        self.reset_position()
        self.old_rect = self.rect.copy()
        self.direction = pygame.Vector2(1, -1).normalize()
        self.speed = self.game.assets["ball_speed"]
        self.launched = False
        
    def reset_position(self):
        """ Position the ball above the bat"""

        self.rect.centerx, self.rect.bottom = self.bat.get_center()
        self.rect.bottom = self.bat.rect.top - 3  # Slightly above the bat
    
    def collision(self, direction):
        for sprite in self.bat_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'vertical':
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.direction.x *= -1
                    
                    if self.rect.left < sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.direction.x *= -1

                    else:
                        if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                            self.rect.bottom = sprite.rect.top
                            self.direction.y *= -1
                        if self.rect.top >= sprite.rect.bottom and self.old_rect.top <= sprite.old_rect.bottom:
                            self.rect.top = sprite.rect.bottom
                            self.direction.y *= -1

    def wall_collision(self):
        #Collision on left and right
        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.direction.x *= -1
        # collision on top and bottom
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.direction.y *= -1



    def move(self, dt):
        if not self.launched:
            # move the ball with bat
            self.reset_position()

        else:
            self.rect.x += self.direction.x * self.game.assets["ball_speed"] * dt  
            self.collision('horizontal')                                  
            self.rect.y += self.direction.y * self.game.assets["ball_speed"] * dt  
            self.collision('vertical')

            self.wall_collision()




    def update(self, dt):
        self.move(dt)

    def launch(self):
        self.launched = True


        