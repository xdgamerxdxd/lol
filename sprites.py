import pygame as pg
from functions import *

global ty
ty = 1040

class Lockscreen(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Lockscreen, self).__init__()
        self.image = pg.image.load('menu/lockscreen.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        
    def run(self, mx, my, click):
        if self.rect.collidepoint((mx, my)):
            if click and my < 1000:
                self.rect.y = my - 1000
        if self.rect.y < -600:
            self.rect.y -= 1000

class Taskbar(pg.sprite.Sprite):
    def __init__(self):
        super(Taskbar, self).__init__()
        self.image = pg.image.load('gui/taskbar.png')
        self.rect = self.image.get_rect()
        self.rect.y = ty

class Windows_Button(pg.sprite.Sprite):
    def __init__(self):
        super(Windows_Button, self).__init__()
        self.image = pg.image.load('icons/wlogo.png')
        self.rect = self.image.get_rect()
        self.rect.y = ty
        self.activ = False
        self.cle = clicke()
    
    def run(self, mx, my, funct, click):
        self.cle.run(self, click, mx, my)

        # if clicked when unactive then make active
        if self.cle.c == 1 and self.activ == False:
            self.cle.c = 0
            self.activ = True 
        # is active
        if self.activ:
            funct.state = True

        # if clicked when active make unactive
        if self.cle.c == 1 and self.activ:
            self.cle.c = 0
            funct.state = False
            self.activ = False
        
class Map_Icon(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Map_Icon, self).__init__()
        self.image = pg.image.load('icons/mapico.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.act = False
    def run(self, mx, my, click):
        if self.rect.collidepoint((mx, my)):
            if click:
                self.act = True
        else:
            self.act = False

class Game_Window(pg.sprite.Sprite):
    def __init__(self, height, width, color):
        super(Game_Window, self).__init__()
        self.image = pg.Surface((width + 1000, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottom = ty / 2
    def run(self, x, y):
        self.rect.x = x
        self.rect.y = y + 40

class Window_Taskbar(pg.sprite.Sprite):
    def __init__(self, width, x, y):
        super(Window_Taskbar, self).__init__()
        self.image = pg.Surface((width, 40))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.drag = False
        self.x = x
        self.y = y
        self.r = False

    def run(self, mx, my, click, dx, dy):
        if self.r == True:
            self.rect.x = self.x
            self.rect.y = self.y
        if self.rect.collidepoint((mx, my)):
            if click:
                self.drag = True
            else:
                self.drag = False
        if self.drag == True:
                self.rect.x += dx
                self.rect.y += dy
        self.r = False

class Exit_Button(pg.sprite.Sprite):
    def __init__(self):
        super(Exit_Button, self).__init__()
        self.image = pygame.image.load('icons/ebutton.png')
        self.rect = self.image.get_rect()
        self.active = False

    def run(self, mx, my, click, x, y):
        self.rect.x = x
        self.rect.y = y
        self.active = False
        if self.rect.collidepoint((mx, my)):
            if click:
                self.active = True

class Options(pg.sprite.Sprite):
    def __init__(self, width, height, color):
        super(Options, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottom = ty + 500
        self.state = False

    def run(self):
        
        if self.state == True:
            if self.rect.bottom > ty:
                self.rect.bottom -= 10
        else:
            if self.rect.bottom < ty + 500:
                self.rect.bottom += 10