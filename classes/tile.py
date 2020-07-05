import pygame
import os


class Tile(pygame.sprite.Sprite):
    """This class represents a single brick wall tile """

    def __init__(self, x, y, sprite_name):
        super().__init__()

        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '../sprites', sprite_name)).convert()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
