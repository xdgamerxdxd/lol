import pygame
import time
import sys
from settings import *
from pygame.locals import *
from gamesettings import Settings

class Image_button_maker():
    def __init__(self, img, surface, x, y):
        super(Image_button_maker, self).__init__()
        self.surface = surface
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def button(self):
        self.surface.blit(self.image, self.rect)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

class Button():
    def __init__(self, surface, text, font, color, bcolor, sizex, sizey, x, y):
        button = pygame.Rect(x, y, sizex, sizey)
        self.rect = pygame.draw.rect(surface, bcolor, button)
        draw_text(text, font, color, surface, self.rect.centerx, self.rect.centery)
    


class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.state = True

    def run(self):

        pygame.init()

        font = pygame.font.SysFont('Monocraft', 100)
        afont = pygame.font.SysFont('Monocraft', 140)
        click = False
        while self.state:
            self.screen.fill((100, 100, 100))
            mx, my = pygame.mouse.get_pos()
            
            draw_text('GAME NAME', afont, (255, 255, 255), self.screen, 960, 200)
            
            button = Button(self.screen, 'START', font, (255, 255, 255), (0, 0, 0), 700, 100, 620, 400)
            button1 = Button(self.screen, 'SETTINGS', font, (255, 255, 255), (0, 0, 0), 700, 100, 620, 600)
            button2 = Button(self.screen, 'QUIT', font, (255, 255, 255), (0, 0, 0), 700, 100, 620, 800)

            if button1.rect.collidepoint((mx, my)):
                if click:
                    self.settings()

            if button2.rect.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()

    def settings(self):
        settings = Settings(self.screen)
        settings.state = True
        settings.run()