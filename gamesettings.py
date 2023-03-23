import pygame
import time
import sys
from pygame.locals import *

class Image_button_maker():
    def __init__(self, img, surface, x, y):
        super(Image_button_maker, self).__init__()
        self.surface = surface
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def button(self):
        self.surface.blit(self.image, self.rect)

class Button():
    def __init__(self, surface, text, font, color, bcolor, sizex, sizey, x, y):
        button = pygame.Rect(x, y, sizex, sizey)
        self.rect = pygame.draw.rect(surface, bcolor, button)
        draw_text(text, font, color, surface, self.rect.centerx, self.rect.centery)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

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