from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import time
import pygame

from cursor import Cursor
from enemy import Enemy

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.toggle_fullscreen()

icon = pygame.image.load(f'assets\\images\\icon.png').convert_alpha()
backgroung_image = pygame.image.load(f'assets\\images\\background.png').convert_alpha()

dummy_texture = pygame.image.load(f'assets\\images\\dummy1.png').convert_alpha()

pygame.display.set_caption("SHOOT 'EM")
pygame.display.set_icon(icon)

cursor = Cursor()

class Dummy(Enemy):
    def __init__(self, pos, size):
        super().__init__(pos, size, dummy_texture, screen)

framerate = 60
clock = pygame.time.Clock()
running = True
last_time = time.time()

dummy = Dummy([30, 30], [40, 240])

script = [[[-1, 0], 100, 0.1], [[1, 0], 100, 0.1]]
slen = len(script)
steps = 0

while running:

    dt = time.time() - last_time
    last_time = time.time()
    dt *= framerate

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
    dummy.render()

    dummy.update(dt)

    pygame.display.flip()
    clock.tick(framerate)

    if not(dummy.moving):
        steps += 1
        a = script[steps%slen][0]
        b = script[steps%slen][1]
        c = script[steps%slen][2]
        dummy.move(a, b, c)

pygame.quit()