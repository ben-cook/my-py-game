import pygame
import os
from config import TILE_WIDTH


class Tile(pygame.sprite.Sprite):
    """This class represents a single tile """

    def __init__(self, x, y, sprite_name):
        super().__init__()

        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '../sprites', sprite_name)).convert()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.rect.width = TILE_WIDTH
        self.rect.height = TILE_WIDTH

    def draw_to_screen(self, screen):
        # new_tile_img = pygame.image.load(os.path.join(os.path.dirname(__file__), '../sprites', 'bg-1.png')).convert()
        screen.blit(self.image, (self.rect.x, self.rect.y))
