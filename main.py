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

class Text():
    _font =  {
        " ": pygame.image.load("assets\\font\\font_.png").convert_alpha(),
        ":": pygame.image.load("assets\\font\\font_dd.png").convert_alpha(),
        "?": pygame.image.load("assets\\font\\font_qm.png").convert_alpha(),
        "*": pygame.image.load("assets\\font\\font_sm.png").convert_alpha(),
        "-": pygame.image.load("assets\\font\\font-.png").convert_alpha(),
        ",": pygame.image.load("assets\\font\\font,.png").convert_alpha(),
        ";": pygame.image.load("assets\\font\\font;.png").convert_alpha(),
        "!": pygame.image.load("assets\\font\\font!.png").convert_alpha(),
        ".": pygame.image.load("assets\\font\\font..png").convert_alpha(),
        "(": pygame.image.load("assets\\font\\font(.png").convert_alpha(),
        ")": pygame.image.load("assets\\font\\font).png").convert_alpha(),
        "@": pygame.image.load("assets\\font\\font@.png").convert_alpha(),
        "&": pygame.image.load("assets\\font\\font&.png").convert_alpha(),
        "#": pygame.image.load("assets\\font\\font#.png").convert_alpha(),
        "%": pygame.image.load("assets\\font\\font%.png").convert_alpha(),
        "^": pygame.image.load("assets\\font\\font^.png").convert_alpha(),
        "+": pygame.image.load("assets\\font\\font+.png").convert_alpha(),
        "=": pygame.image.load("assets\\font\\font=.png").convert_alpha(),
        "$": pygame.image.load("assets\\font\\font$.png").convert_alpha(),
        "0": pygame.image.load("assets\\font\\font0.png").convert_alpha(),
        "1": pygame.image.load("assets\\font\\font1.png").convert_alpha(),
        "2": pygame.image.load("assets\\font\\font2.png").convert_alpha(),
        "3": pygame.image.load("assets\\font\\font3.png").convert_alpha(),
        "4": pygame.image.load("assets\\font\\font4.png").convert_alpha(),
        "5": pygame.image.load("assets\\font\\font5.png").convert_alpha(),
        "6": pygame.image.load("assets\\font\\font6.png").convert_alpha(),
        "7": pygame.image.load("assets\\font\\font7.png").convert_alpha(),
        "8": pygame.image.load("assets\\font\\font8.png").convert_alpha(),
        "9": pygame.image.load("assets\\font\\font9.png").convert_alpha(),
        "A": pygame.image.load("assets\\font\\fontA.png").convert_alpha(),
        "B": pygame.image.load("assets\\font\\fontB.png").convert_alpha(),
        "C": pygame.image.load("assets\\font\\fontC.png").convert_alpha(),
        "D": pygame.image.load("assets\\font\\fontD.png").convert_alpha(),
        "E": pygame.image.load("assets\\font\\fontE.png").convert_alpha(),
        "F": pygame.image.load("assets\\font\\fontF.png").convert_alpha(),
        "G": pygame.image.load("assets\\font\\fontG.png").convert_alpha(),
        "H": pygame.image.load("assets\\font\\fontH.png").convert_alpha(),
        "I": pygame.image.load("assets\\font\\fontI.png").convert_alpha(),
        "J": pygame.image.load("assets\\font\\fontJ.png").convert_alpha(),
        "K": pygame.image.load("assets\\font\\fontK.png").convert_alpha(),
        "L": pygame.image.load("assets\\font\\fontL.png").convert_alpha(),
        "M": pygame.image.load("assets\\font\\fontM.png").convert_alpha(),
        "N": pygame.image.load("assets\\font\\fontN.png").convert_alpha(),
        "O": pygame.image.load("assets\\font\\fontO.png").convert_alpha(),
        "P": pygame.image.load("assets\\font\\fontP.png").convert_alpha(),
        "Q": pygame.image.load("assets\\font\\fontQ.png").convert_alpha(),
        "R": pygame.image.load("assets\\font\\fontR.png").convert_alpha(),
        "S": pygame.image.load("assets\\font\\fontS.png").convert_alpha(),
        "T": pygame.image.load("assets\\font\\fontT.png").convert_alpha(),
        "U": pygame.image.load("assets\\font\\fontU.png").convert_alpha(),
        "V": pygame.image.load("assets\\font\\fontV.png").convert_alpha(),
        "W": pygame.image.load("assets\\font\\fontW.png").convert_alpha(),
        "X": pygame.image.load("assets\\font\\fontX.png").convert_alpha(),
        "Y": pygame.image.load("assets\\font\\fontY.png").convert_alpha(),
        "Z": pygame.image.load("assets\\font\\fontZ.png").convert_alpha(),
        "А": pygame.image.load("assets\\font\\fontА.png").convert_alpha(),
        "Б": pygame.image.load("assets\\font\\fontБ.png").convert_alpha(),
        "В": pygame.image.load("assets\\font\\fontВ.png").convert_alpha(),
        "Г": pygame.image.load("assets\\font\\fontГ.png").convert_alpha(),
        "Д": pygame.image.load("assets\\font\\fontД.png").convert_alpha(),
        "Е": pygame.image.load("assets\\font\\fontЕ.png").convert_alpha(),
        "Ж": pygame.image.load("assets\\font\\fontЖ.png").convert_alpha(),
        "З": pygame.image.load("assets\\font\\fontЗ.png").convert_alpha(),
        "И": pygame.image.load("assets\\font\\fontИ.png").convert_alpha(),
        "Й": pygame.image.load("assets\\font\\fontЙ.png").convert_alpha(),
        "К": pygame.image.load("assets\\font\\fontК.png").convert_alpha(),
        "Л": pygame.image.load("assets\\font\\fontЛ.png").convert_alpha(),
        "М": pygame.image.load("assets\\font\\fontМ.png").convert_alpha(),
        "Н": pygame.image.load("assets\\font\\fontН.png").convert_alpha(),
        "О": pygame.image.load("assets\\font\\fontО.png").convert_alpha(),
        "П": pygame.image.load("assets\\font\\fontП.png").convert_alpha(),
        "Р": pygame.image.load("assets\\font\\fontР.png").convert_alpha(),
        "С": pygame.image.load("assets\\font\\fontС.png").convert_alpha(),
        "Т": pygame.image.load("assets\\font\\fontТ.png").convert_alpha(),
        "У": pygame.image.load("assets\\font\\fontУ.png").convert_alpha(),
        "Ф": pygame.image.load("assets\\font\\fontФ.png").convert_alpha(),
        "Х": pygame.image.load("assets\\font\\fontХ.png").convert_alpha(),
        "Ц": pygame.image.load("assets\\font\\fontЦ.png").convert_alpha(),
        "Ч": pygame.image.load("assets\\font\\fontЧ.png").convert_alpha(),
        "Ш": pygame.image.load("assets\\font\\fontШ.png").convert_alpha(),
        "Щ": pygame.image.load("assets\\font\\fontЩ.png").convert_alpha(),
        "Ъ": pygame.image.load("assets\\font\\fontЪ.png").convert_alpha(),
        "Ы": pygame.image.load("assets\\font\\fontЫ.png").convert_alpha(),
        "Ь": pygame.image.load("assets\\font\\fontЬ.png").convert_alpha(),
        "Э": pygame.image.load("assets\\font\\fontЭ.png").convert_alpha(),
        "Ю": pygame.image.load("assets\\font\\fontЮ.png").convert_alpha(),
        "Я": pygame.image.load("assets\\font\\fontЯ.png").convert_alpha(),
        }
    _text_color = [0,0,0,0]
    
    text = ""

    def __init__(self):
        pass

    def set(self, text):
        self.text = text.upper()

    def draw(self, surf, pos, scale = 1.0, shaking = True, shadowing = True):
        x = 0
        y = 0
        dx = 0
        dy = 0
        for c in self.text:
            if c == "\n":
                y += 1
                x = 0
                continue

            if shaking:
                if random.randint(-100, 100) in [0,1]:
                    dx = random.random()*2
                    dy = random.random()*2
            
            letter = pygame.transform.scale_by(self._font[c], scale)
            if shadowing:
                shadow = pygame.mask.from_surface(letter).to_surface(setcolor=(1, 0, 0, 100))
                shadow.set_colorkey((0,0,0,0))
                surf.blit(shadow, [pos[0]+dx+x*8*scale+2, pos[1]+dy+y*8*scale+2])
            
            surf.blit(letter, [pos[0]+dx+x*8*scale, pos[1]+dy+y*8*scale])
            x += 1

text = Text()
text.set("Привет, друг! \nЯ тоже друг!")

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
    text.draw(screen, [50, 50], 1.8, True)

    pygame.display.flip()
    clock.tick(framerate)

    steps += 1
    if steps >= 1000000:
        steps = 0

pygame.quit()