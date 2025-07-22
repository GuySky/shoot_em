from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import json
import random

from cursor import Cursor
from levels import Map, Level

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.toggle_fullscreen()

from text import Text

icon = pygame.image.load(f'assets\\images\\icon.png').convert_alpha()
backgroung_image = pygame.image.load(f'assets\\images\\background.png').convert_alpha()

pygame.display.set_caption("SHOOT 'EM")
pygame.display.set_icon(icon)

#   =   CURSOR  =   =   =   =   =   =   =   =   =   =   =
cursor = Cursor()
#   =   /CURSOR =   =   =   =   =   =   =   =   =   =   =

#   =   LEVELS  =   =   =   =   =   =   =   =   =   =   =
test_level = Level(json.load(open(f'scripts\\test_lvl.json')))
test_level.load(screen)

chart = Map()
chart.add_level(test_level)
#   =   /LEVELS =   =   =   =   =   =   =   =   =   =   =

#   =   TEXT    =   =   =   =   =   =   =   =   =   =   =
text = Text()
text.set(" :?*-,;!.()@&#%^+=$0123456789 \nabcdefghijklmnopqrstuvwxyz \nабвгдежзийклмнопрстуфхцчшщъыьэюя")
#   =   /TEXT   =   =   =   =   =   =   =   =   =   =   =

framerate = 60
clock = pygame.time.Clock()
running = True

#   =   MENU    =   =   =   =   =   =   =   =   =   =   =
pause_background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
pause_background.fill([0, 0, 0])
pause_background.set_alpha(100)

button_play = pygame.image.load(f'assets//images//play_button.png').convert_alpha()
button_quit = pygame.image.load(f'assets//images//quit_button.png').convert_alpha()

button_play_br = button_play.get_bounding_rect().scale_by(1.03, 1.05).move(120, 45)
button_quit_br = button_quit.get_bounding_rect().scale_by(1.03, 1.05).move(120, 95)

def pause(screen_copy):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
        
        screen.blit(screen_copy)
        screen.blit(pause_background)

        if (button_play_br.collidepoint(pygame.mouse.get_pos())):
            pygame.draw.rect(screen, [195,163,138], button_play_br, 0, 2)
            if pygame.mouse.get_just_pressed()[0]:
                paused = False

        if (button_quit_br.collidepoint(pygame.mouse.get_pos())):
            pygame.draw.rect(screen, [195,163,138], button_quit_br, 0, 2)
            if pygame.mouse.get_just_pressed()[0]:
                return True
        
        screen.blit(button_play, (120, 45))
        screen.blit(button_quit, (120, 95))

        pygame.display.flip()
        clock.tick(framerate)
    
    return False
#   =   /MENU   =   =   =   =   =   =   =   =   =   =   =

# class Game():

#     def __init__(self):
#         pass

#     def loop(self):
#         pass

steps = 0
while running:

#   =   KEYS MANAGEMENT     =   =   =   =   =   =   =   =
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                cursor.stop_reload()
                if pause(screen.copy()):
                    running = False
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_r:
                cursor.reload()
            if event.key == pygame.K_c:
                color = [random.randint(0, 255), 
                         random.randint(0, 255), 
                         random.randint(0, 255), 
                         255]
                text.change_color(color)
#   =   /KEYS MANAGEMENT    =   =   =   =   =   =   =   =

#   =   DRAWING     =   =   =   =   =   =   =   =   =   =
    cursor.update()
    screen.blit(backgroung_image)
    test_level.update(steps)
    text.draw(screen, [10, 10], 1, True)
#   =   /DRAWING    =   =   =   =   =   =   =   =   =   =

#   =   UPDATE      =   =   =   =   =   =   =   =   =   = 
    pygame.display.flip()
    clock.tick(framerate)

    steps += 1
    if steps >= 1000000:
        steps = 0
#   =   /UPDATE     =   =   =   =   =   =   =   =   =   =

# game = Game()
# game.loop()

pygame.quit() 