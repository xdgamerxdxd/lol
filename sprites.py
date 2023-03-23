import pygame

class Lockscreen(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Lockscreen, self).__init__()
        self.image = pygame.image.load('menu/lockscreen.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        
    def run(self, mx, my, click):
        if self.rect.collidepoint((mx, my)):
            if click and my < 1000:
                self.rect.y = my - 1000
        if self.rect.y < -760:
            self.rect.y -= 500