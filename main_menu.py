import pygame
import sys
from game import *
from sprites import *
from settings import *
from functions import *
from pygame.locals import *
from gamesettings import Settings

global m
m = 'menu/'

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
        afont = pygame.font.SysFont(None, 35)
        set = Image_button_maker(f'{m}cogwheel.png', self.screen, 1870, 1030)
        click = False
        while self.state:
            pygame.Surface.blit(self.screen, pygame.image.load(f'{m}lockscreenb.png'), (0, 0))
            pygame.Surface.blit(self.screen, pygame.image.load(f'{m}user.png'), (840, 300))
            draw_text('Create user', font, (255, 255, 255), self.screen, 920, 500)
            set.run()
            btn = Button(self.screen, '', afont, (255, 255, 255), (100, 100, 100), 206, 46, 817, 547)
            button = Button(self.screen, '', afont, (255, 255, 255), (100, 100, 100), 205, 46, 817, 597)
            button1 = Button(self.screen, '', afont, (255, 255, 255), (100, 100, 100), 75, 46, 1000, 597)

            for box in self.input_boxes:
                box.draw(self.screen)
            self.all.draw(self.screen)
            mx, my = pygame.mouse.get_pos()
            self.l.run(mx, my, click)

            if button1.rect.collidepoint((mx, my)):
                if click:
                    self.game()
                
            if set.rect.collidepoint((mx, my)):
                if click:
                    self.settings()

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
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.state = False
        
                for box in self.input_boxes:
                    box.handle_event(event)

            for box in self.input_boxes:
                box.update()
            
            pygame.display.update()

    def settings(self):
        settings = Settings(self.screen)
        settings.state = True
        settings.run()
    
    def game(self):
        game = Game(self.screen)
        game.state = True
        game.run()

def game():

    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
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