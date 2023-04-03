import pygame

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
                if event.key == pygame.K_BACKSPACE:
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

class clicke():
    def __init__(self):
        self.c = 0
        self.cl = False
    
    def run(self, funct, click, mx, my,):
        
        # if on function
        if funct.rect.collidepoint((mx, my)):
            # if click down add 0.5 and activate cl
            if click and self.cl == False:
                self.cl = True
                self.c += 0.5
            # if click add another 0.5 and deactivate cl
            if self.cl == True and click == False:
                self.c += 0.5
                self.cl = False

        # if cl is true and mouse not on function and click or unclik make c 0 and deactivate cl
        if self.cl == True and click == False and funct.rect.collidepoint((mx, my)) == False or self.cl == True and click and funct.rect.collidepoint((mx, my)) == False:
            self.c = 0
            self.cl = False