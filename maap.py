import pygame as pg

class Map(pg.sprite.Sprite):
    def __init__(self):
        super(Map, self).__init__()

        self.image = pg.image.load('map/map1.png')
        self.rect = self.image.get_rect()

    def run(self, x, y):
            self.rect.x = x
            self.rect.y = y + 40

class House(pg.sprite.Sprite):
    def __init__(self):
        super(House, self).__init__()

        self.image = pg.image.load('map/house.png')
        self.rect = self.image.get_rect()

    def run(self, x, y, my, mx):
        self.image = pg.image.load('map/house.png')
        
        self.rect.x = x
        self.rect.y = y + 40

        if self.rect.collidepoint((mx, my)):
            self.image = pg.image.load('map/houseb.png')
        self.rect.x -= 5
        self.rect.y -= 5

class Rhouse (pg.sprite.Sprite):
    def __init__(self):
        super(Rhouse, self).__init__()

        self.image = pg.image.load('map/rhouse.png')
        self.rect = self.image.get_rect()

    def run(self, x, y, my ,mx ):
        self.image = pg.image.load('map/rhouse.png')

        self.rect.x = x
        self.rect.y = y + 40

        if self.rect.collidepoint((mx, my)):
            self.image = pg.image.load('map/rhouseb.png')
            self.rect.x -= 10
            self.rect.y -= 15


class Boss(pg.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()

        self.image = pg.image.load('map/map1.png')
        self.rect = self.image.get_rect()
        
    def run(self, x, y, my, mx):
        self.image = pg.image.load('map/boss.png')

        self.rect.x = x
        self.rect.y = y + 40

        if self.rect.collidepoint((mx, my)):
            self.image = pg.image.load('map/bossb.png')
            self.rect.x -= 10
            self.rect.y -= 15
