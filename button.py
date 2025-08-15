from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

class Button():
    id = ''
    selection = pygame.image.load(f'assets//images//buttons//selection.png').convert_alpha()
    selection_pos = [0, 0]
    texture_rus = pygame.image.load(f'assets//images//buttons//plug.png').convert_alpha()
    texture_eng = pygame.image.load(f'assets//images//buttons//plug.png').convert_alpha()
    pos = [0,0]
    size = [0,0]
    scale = 1
    mouse_pos = [0,0]

    def __init__(self, txtr_rus, txtr_eng, id = 'null'):
        self.texture_rus = pygame.image.load(txtr_rus).convert_alpha()
        self.texture_eng = pygame.image.load(txtr_eng).convert_alpha()
        self.size = self.texture_rus.size
        self.selection = pygame.transform.scale(self.selection, [self.size[0]+6, self.size[1]+6])
        self.selection_pos = [0,0]
        self.mouse_pos = [-1,-1]
        self.id = id

    def set_pos(self, pos):
        self.pos = pos
        self.selection_pos = [pos[0]-3, pos[1]-3]
        self.mouse_pos = [-1,-1]
    
    def scale_by(self, times : float):
        self.size = [self.size[0]*times, self.size[1]*times]
        self.texture_rus = pygame.transform.scale_by(self.texture_rus, times)
        self.texture_eng = pygame.transform.scale_by(self.texture_eng, times)
        self.selection = pygame.transform.scale(self.selection, [self.size[0]+(6*times), self.size[1]+(6*times)])
        self.selection_pos = [self.selection_pos[0]-times-1, self.selection_pos[1]-times-1]
    
    def collide_pt(self, pos) -> bool:
        if pos == self.mouse_pos:
            return False
        if ((self.pos[0] < pos[0]) & (self.pos[0]+self.size[0] > pos[0])) & ((self.pos[1] < pos[1]) & (self.pos[1]+self.size[1] > pos[1])):
            return True
        self.mouse_pos = pos
        return False

    def render(self, surf, lang, mouse_pos) -> bool:
        collide = False
        if (self.collide_pt(mouse_pos)):
            surf.blit(self.selection, self.selection_pos)
            collide = True
        if lang == 'rus':
            surf.blit(self.texture_rus, self.pos)
        if lang == 'eng':
            surf.blit(self.texture_eng, self.pos)
        return collide

if __name__ == '__main__':
    print('Hello from button.py')