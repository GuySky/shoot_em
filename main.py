from os import environ

import json

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from cursor import Cursor
from levels import Map, Level

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.toggle_fullscreen()

icon = pygame.image.load(f'assets\\images\\icon.png').convert_alpha()
backgroung_image = pygame.image.load(f'assets\\images\\background.png').convert_alpha()

pygame.display.set_caption("SHOOT 'EM")
pygame.display.set_icon(icon)

cursor = Cursor()

framerate = 60
clock = pygame.time.Clock()
running = True

test_level = Level(json.load(open(f'scripts\\test_lvl.json')))
test_level.load(screen)

chart = Map()
chart.add_level(test_level)

steps = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                cursor.stop_reload()
                running = False
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_r:
                cursor.reload()

    cursor.update()

    screen.blit(backgroung_image)
    test_level.update(steps)

    pygame.display.flip()
    clock.tick(framerate)

    steps += 1
    if steps >= 1000000:
        steps = 0

pygame.quit()