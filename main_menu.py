import pygame
import sys
from sprites import *
from settings import *
from pygame.locals import *
from gamesettings import Settings

global m
m = 'menu/'

class Image_button_maker():
    def __init__(self, img, surface, x, y):
        super(Image_button_maker, self).__init__()
        self.surface = surface
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def run(self):
        self.surface.blit(self.image, self.rect)


class InputBox():
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('Gray')
        self.text = text
        self.text1 = ''
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint((event.pos)):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color('White') if self.active else pygame.Color('Gray')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

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
        self.entities()
    
    def entities(self):
        self.all = pygame.sprite.Group()
        self.inputbox = InputBox(820, 550, 900, 40, pygame.font.SysFont(None, 32), 'username')
        self.inputbox1 = InputBox(820, 600, 900, 40, pygame.font.SysFont(None, 32), 'password')
        self.input_boxes = [self.inputbox, self.inputbox1]
        self.l = Lockscreen(960, 540)
        self.all.add(self.l)



    def run(self):
        font = pygame.font.SysFont(None, 70)
        afont = pygame.font.SysFont('Monocraft', 140)
        click = False
        while self.state:
            pygame.Surface.blit(self.screen, pygame.image.load(f'{m}lockscreenb.png'), (0, 0))
            pygame.Surface.blit(self.screen, pygame.image.load(f'{m}user.png'), (840, 300))
            draw_text('Create user', font, (255, 255, 255), self.screen, 920, 500)
            for box in self.input_boxes:
                box.draw(self.screen)
            self.all.draw(self.screen)
            mx, my = pygame.mouse.get_pos()
            self.l.run(mx, my, click)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False
    
                for box in self.input_boxes:
                    box.handle_event(event)

            for box in self.input_boxes:
                box.update()
            
            pygame.display.update()

    def settings(self):
        settings = Settings(self.screen)
        settings.state = True
        settings.run()

def game():

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    game = Menu(screen)
    
    while game.state:
        screen.fill([0, 0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.run()

        pygame.display.update()
        clock.tick(30)
        pygame.display.flip()

    pygame.quit()
game()