import pygame
from pygame.locals import *
from functions import *

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
        while self.state:
            self.screen.fill((50, 50, 50))
            map.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            pygame.display.update()