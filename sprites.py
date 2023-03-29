import pygame
from functions import *

global ty
ty = 1040

class Lockscreen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Lockscreen, self).__init__()
        self.image = pygame.image.load('menu/lockscreen.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        
    def run(self, mx, my, click):
        if self.rect.collidepoint((mx, my)):
            if click and my < 1000:
                self.rect.y = my - 1000
        if self.rect.y < -600:
            self.rect.y -= 1000

class Taskbar(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super(Taskbar, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = ty
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Windows_Button(pygame.sprite.Sprite):
    def __init__(self):
        super(Windows_Button, self).__init__()
        self.image = pygame.image.load('icons/wlogo.png')
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
        








class Options(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super(Options, self).__init__()
        self.image = pygame.Surface((width, height))
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