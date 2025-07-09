from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from enemy import Enemy

class Map:
    running = False
    level_list = []
    level_cur = 0

    def __init__(self):
        pass

    def add_level(self, level):
        self.level_list.append(level)

class Level(Map):
    _enemies = []
    _active_enemies = []
    _file = {}

    def __init__(self, file):
        self._file = file

    def get_enemies(self):
        return self._enemies
    
    def get_active_enemies(self):
        return self._active_enemies

    def load(self, display):
        self._enemies = []
        level = self._file
        for key in level:
            pos = level[key][0]
            size = level[key][1]
            texture = pygame.image.load(level[key][2]).convert_alpha()
            script = level[key][3]
            spawn_time = level[key][4]

            new_enemy = Enemy(pos, size, texture, display)
            enemy = [new_enemy, spawn_time]
            enemy[0].add_script(script)
            self._enemies.append(enemy)

    def update(self, steps):
        for enemy in self._enemies:
            if (steps >= enemy[1]):
                self._active_enemies.append(enemy[0])
                enemy[1] = 1000001

        for enemy in self._active_enemies:
            enemy.update()
            enemy.render()