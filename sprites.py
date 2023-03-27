import pygame

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
        self.wbutton = Windows_Button()
    
    def draw(self, screen, click):
        mx, my = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)
        screen.blit(self.wbutton.image, self.wbutton.rect)
        self.wbutton.run(click, screen, mx, my)

class Windows_Button(pygame.sprite.Sprite):
    def __init__(self):
        super(Windows_Button, self).__init__()
        self.image = pygame.image.load('icons/wlogo.png')
        self.rect = self.image.get_rect()
        self.rect.y = ty
        self.state = False

    def run(self, click, screen, mx, my):
        opt = Options(400, 500, (55, 55, 55))
        if self.rect.collidepoint((mx, my)):
            if click:
                self.state = True
                click = False
        if self.state == True:
            opt.draw(screen)
            if self.state == True and click:
                self.state = False






class Options(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super(Options, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottom = ty + 500

    def draw(self, screen):
        while self.rect.bottom > ty:
            self.rect.bottom -= 1
            screen.blit(self.image, self.rect)