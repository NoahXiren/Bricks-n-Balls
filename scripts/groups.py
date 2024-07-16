import pygame

class Allsprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()


    def draw(self):
        #shadow
        for sprite in self:
            self.screen.blit(sprite.shadow_surf, sprite.rect.topleft + pygame.Vector2(5,5))

        # custom draw method
        for sprite in self:
            self.screen.blit(sprite.image, sprite.rect)