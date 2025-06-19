import pygame

class Enemy:
    _pos = [0, 0]
    _size = [0, 0]

    _steps = 0
    _half = 0
    _dir = [0, 0]
    _dest = 0

    _speed = 0
    _accel = 0
    moving = False

    texture = pygame.Surface([0,0])
    texture_copy = pygame.Surface([0,0])
    display_surface = pygame.Surface([0,0])
    target = pygame.Rect()

    def __init__(self, pos : list, size : list, texture : pygame.Surface, display_surface : pygame.Surface):
        self._pos = pos
        self._size = size
        self.texture = texture
        self.texture_copy = texture
        self.shadow = pygame.mask.from_surface(self.texture_copy).to_surface(setcolor=(0, 0, 1, 150))
        self.shadow.set_colorkey((0,0,0,0))
        self.display_surface = display_surface
        self.taget = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def get_pos(self):
        return self._pos

    def render(self):
        self.display_surface.blit(self.shadow, [self.taget[0]+10, self.taget[1]+5])
        self.display_surface.blit(self.texture_copy, self.taget)

    def move(self, dir : list, steps : int, accel : float):
        self.moving = True
        self._speed = 0
        self._steps = 0
        self._dir = dir
        self._dest = steps
        self._half = steps//2
        self._accel = accel

    def update(self, dt):
        if self.moving:
            if self._steps > self._half:
                self._accel *= (-1)
                self._half = self._dest
            
            self._speed += self._accel
            
            t0 =  self._dir[0] * self._speed * dt
            t1 =  self._dir[1] * self._speed * dt

            self.texture_copy = pygame.transform.smoothscale(self.texture, [self._size[0]+(self._speed*dt), self._size[1]+(self._speed*dt)])
            self._pos[0] += t0
            self._pos[1] += t1
            self.taget = self.taget.move([t0, t1])

            if (self._steps == self._dest):
                self.moving = False
                self.texture_copy = self.texture
            
            self._steps += 1