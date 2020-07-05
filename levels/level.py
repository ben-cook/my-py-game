import pygame
import math
import os

from levels.levels import level_one, level_two
from classes.tile import Tile


class Level():
    """ This class represents a level """

    def __init__(self, level_number):

        self.wall_tiles = pygame.sprite.Group()
        self.bg_tiles = pygame.sprite.Group()

        if level_number == 1:
            for j in range(0, 25):
                for i in range(0, 25):
                    if level_one[j][i] == 0:
                        self.bg_tiles.add(Tile(i * 32, j * 32, 'bg-2.png'))
                    if level_one[j][i] == 1:
                        self.wall_tiles.add(Tile(i * 32, j * 32, 'bg-3.png'))
                    if level_one[j][i] == 2:
                        self.wall_tiles.add(Tile(i * 32, j * 32, 'grass.png'))

        if level_number == 2:
            for j in range(0, 25):
                for i in range(0, 25):
                    if level_two[j][i] == 0:
                        self.bg_tiles.add(Tile(i * 32, j * 32, 'bg-2.png'))
                    if level_two[j][i] == 1:
                        self.wall_tiles.add(Tile(i * 32, j * 32, 'bg-3.png'))
                    if level_two[j][i] == 2:
                        self.wall_tiles.add(Tile(i * 32, j * 32, 'grass.png'))

    def draw_walls(self, screen):
        self.wall_tiles.draw(screen)

    def draw_bg_tiles(self, screen):
        self.bg_tiles.draw(screen)
