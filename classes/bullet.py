import pygame
import math
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BLACK = (0, 0, 0)


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """

    def __init__(self, start_x, start_y, dest_x, dest_y):
        """ Constructor.
        It takes in the starting x and y location.
        It also takes in the destination x and y position.
        """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set up the image for the bullet
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), '..\sprites', 'bullet.png')).convert_alpha()

        self.rect = self.image.get_rect()

        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y

        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 5
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

    def update(self, walls):
        """ Move the bullet. """

        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        # Did this update cause us to hit a wall?
        wall_hit_list = pygame.sprite.spritecollide(self, walls, False)
        if len(wall_hit_list) != 0:
            self.kill()

        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()
