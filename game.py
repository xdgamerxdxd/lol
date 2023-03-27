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
        pass

    def run(self):
        map = Image_button_maker('icons/mapico.png', self.screen, 50, 50)
        click = False
        task = Taskbar(1920, 40, (55, 55, 55))
        mx, my = pygame.mouse.get_pos()
        while self.state:
            self.screen.fill((0, 0, 0))
            map.run()
            task.draw(self.screen, click)
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