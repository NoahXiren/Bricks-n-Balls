import pygame
from .constant import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, groups, posx, posy, width, height, color):
        super().__init__(groups)
        self.game = game
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
        self.image = 100


        if color == COLOR["obstacle_2"]:
            self.health = 200
        else:
            self.health = 100
# TODO: make the bricks and collision also add scoring system
