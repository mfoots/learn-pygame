import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,600))
win = screen.get_rect()

class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(pygame.Color(255,0,255))
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(win.centerx, win.centery)

    def update(self):
        self.rect.center = self.pos

    def move(self):
        # self.pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pos()
        if self.rect.left < mouse[0] < self.rect.right:
            if self.rect.top < mouse[1] < self.rect.bottom:
                self.pos = mouse

all_sprites = pygame.sprite.RenderPlain()
box = Box()
box.add(all_sprites)
mouse_down = False

running = True
while running:

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == MOUSEBUTTONUP:
            mouse_down = False
    
    if mouse_down:
        box.move()

    all_sprites.update()
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()