import pygame
import math
import os

from levels.levels import level_one, level_two


class Level():
    """ This class represents a level """

    def __init__(self, level_number):
        """ Constructor function """

        self.wall_tiles = pygame.sprite.Group()

        if level_number == 1:
            for j in range(0, 25):
                for i in range(0, 25):
                    if level_one[j][i] == 1:
                        self.wall_tiles.add(WallTile(i * 32, j * 32))

        if level_number == 2:
            for j in range(0, 25):
                for i in range(0, 25):
                    if level_two[j][i] == 1:
                        self.wall_tiles.add(WallTile(i * 32, j * 32))

    def draw_walls(self, screen):
        self.wall_tiles.draw(screen)


class WallTile(pygame.sprite.Sprite):
    """This class represents a single brick wall tile """

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '../sprites', 'brick-wall.png')).convert()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
