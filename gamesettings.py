import pygame
import sys
from functions import *
from pygame.locals import *

class Settings():
    def __init__(self, screen):
        self.screen = screen
        self.state = False

    def run(self):

        pygame.init()

        font = pygame.font.SysFont('Monocraft', 100)
        afont = pygame.font.SysFont('Monocraft', 40)
        click = False
        while self.state:
            self.screen.fill((100, 100, 100))
            mx, my = pygame.mouse.get_pos()
            draw_text('SETTINGS', font, (255, 255, 255), self.screen, 960, 50)
            button = Button(self.screen, 'BACK', font, (255, 255, 255), (0, 0, 0), 300, 100, 1600, 900)
            button1 = Button(self.screen, 'RESOLUTION', font, (255, 255, 255), (0, 0, 0), 700, 100, 100, 200)

            if button.rect.collidepoint((mx, my)):
                if click:
                    self.state = False
            if button1.rect.collidepoint((mx, my)):
                if click:
                    pass

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()