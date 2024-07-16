import pygame
from .constant import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, groups, posx, posy, color):
        super().__init__(groups)
        self.game = game
        self.posx = posx
        self.posy = posy
        self.color = color
        self.damage = 100


        if color == COLOR["obstacle_2"]:
            self.health = 200
        else:
            self.health = 100

        # create the image surface for the obstacles
        self.image = pygame.Surface(self.game.assets["obstacle"], pygame.SRCALPHA)
        # self.image.fill(self.color)
        pygame.draw.rect(self.image,
                         self.color,
                         pygame.FRect((0,0), self.game.assets['obstacle']),
                         0,5) #width and radius


        # mask
        self.mask = pygame.mask.from_surface(self.image)

        # shadow
        self.shadow_surf = self.image.copy()
        pygame.draw.rect(self.shadow_surf,
                           COLOR["shadow"],
                           pygame.FRect((0,0), self.game.assets["obstacle"]),
                           0,5)
        # set the initial position of the obstacles
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posx, self.posy)

    def update(self, dt):
        pass

    def hit(self):
        self.health -= self.damage

    def get_health(self):
        return self.health