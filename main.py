from os import environ

import json

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import time
import pygame

from cursor import Cursor
from enemy import Enemy

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
#pygame.display.toggle_fullscreen()

icon = pygame.image.load(f'assets\\images\\icon.png').convert_alpha()
backgroung_image = pygame.image.load(f'assets\\images\\background.png').convert_alpha()

pygame.display.set_caption("SHOOT 'EM")
pygame.display.set_icon(icon)

cursor = Cursor()

framerate = 60
clock = pygame.time.Clock()
running = True
last_time = time.time()

level = json.load(open(f'scripts\\test_lvl.json'))
enemies = []
for key in level:
    pos = level[key][0]
    size = level[key][1]
    texture = pygame.image.load(level[key][2]).convert_alpha()
    script = level[key][3]
    spawn_time = level[key][4]

    new_enemy = Enemy(pos, size, texture, screen)
    enemy = [new_enemy, spawn_time]
    enemy[0].add_script(script)
    enemies.append(enemy)

active_enemies = []

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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_just_pressed()[0]:
                pass

    cursor.update()

    screen.blit(backgroung_image)

    for enemy in enemies:
        if (steps >= enemy[1]):
            active_enemies.append(enemy[0])
            enemy[1] = 1000001

    for enemy in active_enemies:
        enemy.update()
        enemy.render()

    pygame.display.flip()
    clock.tick(framerate)

    steps += 1
    if steps >= 1000000:
        steps = 0

pygame.quit()