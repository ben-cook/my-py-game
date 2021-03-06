import pygame
import math
import os


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        # self.image = pygame.image.load(os.path.join('.\..\sprites', 'player.png')).convert()
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..\sprites', 'player2.png')).convert_alpha()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def set_direction(self, dir):
        if dir == 'left':
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..\sprites', 'player2_left.png')).convert_alpha()
        elif dir == 'right':
            self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..\sprites', 'player2.png')).convert_alpha()
        else:
            raise ValueError("Invalid direction:" + str(dir))

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
