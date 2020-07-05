import pygame
import os

from config import *
from classes.player import Player
from classes.bullet import Bullet
from levels.level import Level

# Mitchell was here 5/7/2020

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

    font = pygame.font.Font(None, 30)
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
                bullet = Bullet(player.rect.centerx, player.rect.centery, mouse_x, mouse_y)

                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                moving_sprites.add(bullet)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-PLAYER_SPEED, 0)
                    player.set_direction('left')
                if event.key == pygame.K_d:
                    player.changespeed(PLAYER_SPEED, 0)
                    player.set_direction('right')
                if event.key == pygame.K_w:
                    player.changespeed(0, -PLAYER_SPEED)
                if event.key == pygame.K_s:
                    player.changespeed(0, PLAYER_SPEED)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(PLAYER_SPEED, 0)
                if event.key == pygame.K_d:
                    player.changespeed(-PLAYER_SPEED, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, PLAYER_SPEED)
                if event.key == pygame.K_s:
                    player.changespeed(0, -PLAYER_SPEED)

        # --- Game Logic ---

        if level_changed:
            if current_level_x == 0 and current_level_y == 0:
                # print('Entering level 1')
                current_level = Level(1)
            else:
                # print('Entering level 2')
                current_level = Level(2)

            current_level.draw_bg_tiles(screen)
            current_level.draw_walls(screen)
            pygame.display.flip()
            level_changed = False

        # Dirty rects are all the rects that need to be updated at the end of this frame
        dirty_rects = []

        # get tiles intersecting player
        bg_to_draw = []
        for bg_tile in current_level.bg_tiles:
            if bg_tile.rect.colliderect(player.rect):
                bg_to_draw.append(bg_tile)
            for bullet in bullet_list:
                if bg_tile.rect.colliderect(bullet.rect):
                    bg_to_draw.append(bg_tile)

        # add those tiles to dirty rects
        dirty_rects.extend([bg_tile.rect for bg_tile in bg_to_draw])
        dirty_rects.append(player.rect)

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

        # draw walls and player
        for bg_tile in bg_to_draw:
            bg_tile.draw_to_screen(screen)
        for bullet in bullet_list:
            screen.blit(bullet.image, bullet.rect)
        screen.blit(player.image, player.rect)

        # print(dirty_rects)

        if SHOW_FPS:

            fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
            fps_bg_image = pygame.Surface([32, 32])
            fps_bg_image.fill(BLACK)
            screen.blit(fps_bg_image, (0, 0))
            screen.blit(fps, (0, 0))
            dirty_rects.append(fps_bg_image.get_rect())

        pygame.display.update(dirty_rects)

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
