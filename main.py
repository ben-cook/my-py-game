import pygame
import os

from config import *
from classes.player import Player
from classes.bullet import Bullet
from levels.level import Level


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create a 500x500 sized screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("my-py-game")

    # Create the player paddle object
    player = Player(64, 64)

    # List of moving sprites
    moving_sprites = pygame.sprite.Group()
    moving_sprites.add(player)

    # List of all sprites
    all_sprites_list = pygame.sprite.Group()

    # List of all bullets
    bullet_list = pygame.sprite.Group()

    level_changed = True
    current_level_x = 0
    current_level_y = 0

    clock = pygame.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # if event.type == pygame.VIDEORESIZE:
            #     old_screen_saved = screen
            #     screen = pygame.display.set_mode((event.w, event.h),
            #                                      pygame.RESIZABLE)
            #     # On the next line, if only part of the window
            #     # needs to be copied, there's some other options.
            #     screen.blit(old_screen_saved, (0, 0))
            #     del old_screen_saved

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button

                # Get the mouse position
                pos = pygame.mouse.get_pos()

                mouse_x = pos[0]
                mouse_y = pos[1]

                # Create the bullet based on where we are, and where we want to go.
                bullet = Bullet(player.rect.x, player.rect.y, mouse_x, mouse_y)

                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                moving_sprites.add(bullet)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_d:
                    player.changespeed(5, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(5, 0)
                if event.key == pygame.K_d:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        if level_changed:
            if current_level_x == 0 and current_level_y == 0:
                print('Entering level 1')
                current_level = Level(1)
            else:
                print('Entering level 2')
                current_level = Level(2)
            level_changed = False

        player.move(current_level.wall_tiles)

        # Changing between levels
        if player.rect.y < -TILE_WIDTH / 2 and current_level_y == 0:
            level_changed = True
            current_level_y += 1
            player.rect.y = SCREEN_HEIGHT - TILE_WIDTH / 2 - 1

        if player.rect.y > SCREEN_HEIGHT - TILE_WIDTH / 2 and current_level_y > 0:
            level_changed = True
            current_level_y -= 1
            player.rect.y = -TILE_WIDTH / 2 + 1

        for bullet in bullet_list:
            bullet.update(current_level.wall_tiles)

        # --- Drawing ---
        # Background
        bg_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'bg-1.png')).convert()
        brick_tile = pygame.image.load(os.path.join(os.path.dirname(__file__), 'sprites', 'brick-wall.png')).convert()

        for i in range(0, 800, 32):
            for j in range(0, 800, 32):
                screen.blit(bg_tile, (i, j))

        moving_sprites.draw(screen)
        # current_room.wall_list.draw(screen)

        current_level.draw_walls(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
