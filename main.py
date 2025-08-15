from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import json
import random

from cursor import Cursor
from levels import Map, Level

pygame.init()

from text import Text

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 180
display = pygame.display
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)

from button import Button

class Game():
    caption = "SHOOT 'EM"

    screen = screen
    display = display

    language = 'rus'
    runs_count = 0

    _clock = pygame.time.Clock()
    framerate = 60
    running = True

    def __init__(self):
        self.icon = pygame.image.load(f'assets\\images\\icon.png').convert_alpha()
        self.backgroung_image = pygame.image.load(f'assets\\images\\background.png').convert_alpha()

        self.cursor = Cursor()
        self.text = Text()
        self.text.set(" :?*-,;!.()@&#%^+=$0123456789 \nabcdefghijklmnopqrstuvwxyz \nабвгдежзийклмнопрстуфхцчшщъыьэюя")

        self.screen_copy = self.screen.copy()
        self.display.toggle_fullscreen()
        self.display.set_caption(self.caption)
        self.display.set_icon(self.icon)
        self.chart = Map()

    def level(self, level):
        test_level = Level(json.load(open(level)))
        test_level.load(self.screen)
        self.chart.add_level(test_level)
    
    def loop_prescreen(self):
        rus_text = Text('Пожалуйста \nвыберите язык игры')
        rus_text.change_color((255, 255, 255))
        eng_text = Text('Please \nchoose the game language')
        eng_text.change_color((255, 255, 255))

        button_rus = Button(f'assets/images/buttons/flag_rus.png', f'assets/images/buttons/flag_rus.png', 'flag_rus')
        button_eng = Button(f'assets/images/buttons/flag_eng.png', f'assets/images/buttons/flag_eng.png', 'flag_eng')

        buttons = [button_rus, button_eng]

        button_rus.set_pos([60, 80])
        button_eng.set_pos([170, 80])
        button_rus.scale_by(2)
        button_eng.scale_by(2)

        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.collide_pt(mouse_pos):
                            if button.id == 'flag_rus':
                                self.language = 'rus'
                            else:
                                self.language = 'eng'
                            running = False

            self.screen.fill("black")
            
            if button_rus.render(self.screen, 'rus', mouse_pos):
                rus_text.draw(self.screen, [30, 30], 1.4, False)
            if button_eng.render(self.screen, 'eng', mouse_pos):
                eng_text.draw(self.screen, [30, 30], 1.4, False)

            self.display.flip()
            self._clock.tick(self.framerate)

    def loop_menu(self):
        self.runs_count += 1

        black_screen = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
        black_screen.fill([0,0,0])
        

        background = [pygame.image.load('assets//images//menu//background_dummy.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background1.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background2.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background3.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background4.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background5.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background6.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background7.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background8.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background9.png').convert_alpha(),
                      pygame.image.load('assets//images//menu//background10.png').convert_alpha(),
                      ]

        button_play = Button('assets//images//buttons//play_rus.png', 'assets//images//buttons//play_eng.png', 'play')
        button_play.set_pos([20, 20])
        button_settings = Button('assets//images//buttons//settings_rus.png', 'assets//images//buttons//settings_eng.png', 'settings')
        button_settings.set_pos([20, 70])
        button_quit = Button('assets//images//buttons//quit_rus.png', 'assets//images//buttons//quit_eng.png', 'quit')
        button_quit.set_pos([20, 120])

        caption = Text(' shoot \n\'em')
        caption.change_color([246, 214, 189])

        buttons = [button_play, button_settings, button_quit]

        steps = 0
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.collide_pt(mouse_pos):
                            if button.id == 'play':
                                self.loop_chart()
                            elif button.id == 'settings':
                                self.loop_settings()
                            elif button.id == 'quit':
                                running = False

            black_screen.set_alpha(280-steps)

            bg = random.randint(1, 10)
            self.screen.blit(background[bg])
            self.screen.blit(background[0], [random.randint(0, 3), random.randint(0, 3)])

            caption.draw(self.screen, [120, 40], 4)
            
            for button in buttons:
                button.render(self.screen, self.language, mouse_pos)
            
            self.screen.blit(black_screen)

            self.display.flip()
            self._clock.tick(self.framerate)
            steps += 1
            if steps >= 1000000:
                steps = 0

    def loop_chart(self, level = -1):
        if level >= 0:
            self.loop_level(level)

    def loop_settings(self):
        pass

    def loop_level(self, number):
        level_cur = self.chart.level_list[self.chart.level_cur]

        quit = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.cursor.stop_reload()
                        print('pause')
                        if self.loop_pause(self.screen.copy()):
                            quit = True
                            running = False
                    if event.key == pygame.K_F11:
                        pygame.display.toggle_fullscreen()
                    if event.key == pygame.K_r:
                        self.cursor.reload()
                    if event.key == pygame.K_c:
                        color = [random.randint(0, 255), 
                                random.randint(0, 255), 
                                random.randint(0, 255), 
                                255]
                        self.text.change_color(color)

            self.chart.level_list

            self.cursor.update()
            self.screen.blit(self.backgroung_image)
            level_cur.update(self._steps)
            self.text.draw(self.screen, [10, 10], 1, True)
            self.display.flip()
            self._clock.tick(self.framerate)

            self._steps += 1
            if self._steps >= 1000000:
                self._steps = 0

        return quit

    def loop_pause(self, screen_copy):
        quit = False
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    paused = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit = False
                        paused = False
                    if event.key == pygame.K_F11:
                        self.display.toggle_fullscreen()
            
            self.screen.blit(screen_copy)
            # self.screen.blit(self._pause_background)

            # if (self._button_play_br.collidepoint(pygame.mouse.get_pos())):
            #     pygame.draw.rect(self.screen, [195,163,138], self._button_play_br, 0, 2)
            #     if pygame.mouse.get_just_pressed()[0]:
            #         quit = False
            #         paused = False

            # if (self._button_quit_br.collidepoint(pygame.mouse.get_pos())):
            #     pygame.draw.rect(self.screen, [195,163,138], self._button_quit_br, 0, 2)
            #     if pygame.mouse.get_just_pressed()[0]:
            #         quit = True
            #         paused = False
            
            # self.screen.blit(self._button_play, (120, 45))
            # self.screen.blit(self._button_quit, (120, 95))

            self.display.flip()
            self._clock.tick(self.framerate)

        return quit
    
game = Game()
if game.runs_count == 0:
    game.loop_prescreen()
game.loop_menu()

pygame.quit() 