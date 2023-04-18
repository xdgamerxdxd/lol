import pygame
from maap import *
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
        self.gwintb = Window_Taskbar(1400, 500, 100)
        self.exit = Exit_Button()
        self.house = House()
        self.rhouse = Rhouse()
        self.boss = Boss()
        self.maap = Map()
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
            dx, dy = pygame.mouse.get_rel()

            self.screen.fill((45, 45, 45))
            self.all.draw(self.screen)

            self.exit.run(mx, my, click, self.gwintb.rect.x + 1360, self.gwintb.rect.y + 5)
            self.map.run(mx, my, click)
            self.wbutton.run(mx, my, self.opt, click)
            self.gwintb.run(mx, my, click, dx, dy)
            self.maap.run(self.gwintb.rect.x, self.gwintb.rect.y)
            self.house.run(self.gwintb.rect.x + 425, self.gwintb.rect.y + 50, my, mx)
            self.rhouse.run(self.gwintb.rect.x + 870, self.gwintb.rect.y + 550, my, mx)
            self.boss.run(self.gwintb.rect.x + 1225, self.gwintb.rect.y + 75, my, mx)
            self.opt.run()

            if self.map.act == True:
                self.gwintb.r = True
                self.all.add(self.maap, self.gwintb, self.exit, self.house, self.rhouse, self.boss)

            if self.exit.active == True:
                self.all.remove(self.maap, self.gwintb, self.exit, self.house, self.rhouse, self.boss)

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