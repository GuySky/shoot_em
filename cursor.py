from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

class Cursor:
    def __init__(self, size = (25,25), image = f'assets\\cursor\\cursor.png', image_reload = f'assets\\cursor\\cursorr.png'):
        self.size: tuple = size
        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(image).convert_alpha(), self.size)
        self.image_reload: pygame.Surface = pygame.transform.scale(pygame.image.load(image_reload).convert_alpha(), self.size)
        self.image_copy = None
        self.cursor: pygame.Cursor = pygame.cursors.Cursor((size[0]//2 + 1, size[1]//2 + 1), self.image)
        self.cursor_reload: pygame.Cursor = pygame.cursors.Cursor((size[0]//2 + 1, size[1]//2 + 1), self.image)

        self.weapon: int = 0
        self.reloading: bool = False
        
        self.angle: float = 0
        self.speed: float = 5
        self.right: int = -1
        self.accel: float = 1.1

        pygame.mouse.set_cursor(self.cursor)

    def get_weapon(self):
        return self.weapon
    
    def set_weapon(self, weapon: int):
        self.weapon = weapon

    def reload(self):
        self.reloading = True

    def stop_reload(self):
        self.reloading = False
        self.angle = 0
        self.speed = 5
        self.right = -1
        self.accel = 1.1
        self.image_copy = self.image
        pygame.mouse.set_cursor(pygame.cursors.Cursor((self.image.get_size()[0]//2 + 1, self.image_copy.get_size()[1]//2 + 1), self.image))

    def update(self):
        if not(self.reloading):
            return

        self.speed *= self.accel
        self.angle += self.speed*self.right
        self.image_copy = pygame.transform.rotate(self.image_reload, self.angle)
        pygame.mouse.set_cursor(pygame.cursors.Cursor((self.image_copy.get_size()[0]//2 + 1, self.image_copy.get_size()[1]//2 + 1), self.image_copy))

        if self.angle < -(360 - self.weapon*90)*0.5:
            self.accel = 0.9

        if self.angle < -(360 - self.weapon*90):
            self.stop_reload()

if __name__ == '__main__':
    print('Hello from cursor.py')