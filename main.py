from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import time
import pygame

from cursor import Cursor

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.toggle_fullscreen()

icon = pygame.image.load(f'assets\\images\\icon.png').convert_alpha()
backgroung_image = pygame.image.load(f'assets\\images\\background.png').convert_alpha()

dummy_texture = pygame.image.load(f'assets\\images\\dummy1.png').convert_alpha()

pygame.display.set_caption("SHOOT 'EM")
pygame.display.set_icon(icon)

class Enemy:
    _pos = []
    _tagetSize = []

    _speed = 0
    _accel = 0
    _dest = 0
    _dir = []
    moving = False

    def __init__(self, pos : list, size : list, texture, display_surface):
        self._pos = pos
        self._tagetSize = size
        self.texture : pygame.Surface = texture
        self.display_surface : pygame.Surface = display_surface
        self.taget = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def get_pos(self):
        return self._pos
    
    def get_tagetSize(self):
        return self._tagetSize

    def render(self):
        self.display_surface.blit(self.texture, self.taget)

    def move(self, dest, accel, dir):
        self.moving = True
        self._speed = 0
        self._accel = accel
        self._dest = dest/2
        self._dir = dir

    def sway(self, accel, angle):
        pass

    def update(self, dt):
        if self.moving:
            if abs(self._speed) > abs(self._dest):
                self._accel *= (-1)
            self._speed += self._accel
            t0 = self._dir[0] * self._speed * dt
            t1 = self._dir[1] * self._speed * dt

            self._pos[0] += t0
            self._pos[1] += t1
            self.taget = self.taget.move([t0, t1])

            if self._speed < 0:
                self.moving = False

class Dummy(Enemy):
    def __init__(self, pos, size):
        super().__init__(pos, size, dummy_texture, screen)

cursor = Cursor()

framerate = 60
clock = pygame.time.Clock()
running = True
last_time = time.time()

dummy = Dummy([30, 30], [40, 40])

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
            if event.key == pygame.K_m:
                dummy.move(10, 1, [1, 0])

    cursor.update()
    
    screen.blit(backgroung_image)
    dummy.render()

    dummy.update(dt)

    pygame.display.flip()
    clock.tick(framerate)

pygame.quit()