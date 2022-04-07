import pygame
from pygame.locals import *
import math
pygame.init()

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()

# Define Sprite Classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # store the original image
        self.original_image = pygame.image.load('assets/fighter.png').convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=window.center)
        self.speed = 0
        self.vector = pygame.Vector2(0, 0)
        self.angle = 0
        # store the original center point
        self.pivot = pygame.Vector2(self.rect.center)
        self.offset = pygame.Vector2(0, 0)

    def update(self):
        self.rotate()
        self.vector.x += self.speed * math.sin(math.radians(self.angle)) * -1
        self.vector.y += self.speed * math.cos(math.radians(self.angle)) * -1
        self.rect.move_ip(self.vector)

        if self.rect.centery < 0:
            self.rect.move_ip(0, window.height)
            self.vector.y += window.height
        if self.rect.centery > window.height:
            self.rect.move_ip(0, -window.height)
            self.vector.y += -window.height
        if self.rect.centerx < 0:
            self.rect.move_ip(window.width, 0)
            self.vector.x += window.width
        if self.rect.centerx > window.width:
            self.rect.move_ip(-window.width, 0)
            self.vector.x += -window.width

    def move(self):
        self.speed = 5

    def stop(self):
        if self.speed > 0:
            self.speed *= .98
        
    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        # readjust the center of the rectangle
        self.rect = self.image.get_rect(center=self.pivot + self.offset.rotate(self.angle)) # Why?
        self.angle = self.angle % 360


# Create Sprite Objects
ship = Ship()
all_sprites = pygame.sprite.RenderUpdates()
all_sprites.add(ship)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        ship.move()
    else:
        ship.stop()
    if keys[K_RIGHT]:
        ship.angle -= 5
    if keys[K_LEFT]:
        ship.angle += 5

    all_sprites.update()
    

    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
