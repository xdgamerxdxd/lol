import pygame
from settings import *
from main_menu import Menu

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.entities()

    def entities(self):
        pass

    def run(self):
        self.menu()

    def menu(self):
        menu = Menu(self.screen)
        menu.run()

    def restart(self):
        self.entities()

def game():

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    game = Game(screen)
    
    while game.running:
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