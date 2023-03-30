import pygame
from sprites import *
from functions import *
from pygame.locals import *

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.state = False
        self.entities()

    def entities(self):
        self.all = pygame.sprite.Group()
        self.gwindow = Game_Window(500, 500, (100, 100, 100))
        self.gwintb = Window_Taskbar(500, 500, 100)
        self.exit = Exit_Button()
        self.map = Map_Icon(50, 50)
        self.wbutton = Windows_Button()
        self.task = Taskbar()
        self.opt = Options(400, 500, (55, 55, 55))
        self.all.add(self.opt,self.task, self.wbutton, self.map)

    def run(self):
        global mx, my, click
        click = False
        while self.state:
            mx, my = pygame.mouse.get_pos()

            self.screen.fill((45, 45, 45))
            self.all.draw(self.screen)
            
            self.exit.run(mx, my, click, self.gwintb.rect.x + 460, self.gwintb.rect.y + 5)
            self.map.run(mx, my, click)
            self.wbutton.run(mx, my, self.opt, click)
            self.gwintb.run(mx, my, click)
            self.gwindow.run(self.gwintb.rect.x, self.gwintb.rect.y)
            self.opt.run()

            if self.map.act == True:
                self.gwintb.r = True
                self.all.add(self.gwindow, self.gwintb, self.exit)

            if self.exit.active == True:
                self.all.remove(self.gwindow, self.gwintb, self.exit)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.state = False
            pygame.display.update()