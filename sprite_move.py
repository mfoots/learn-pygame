import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()

# Define Sprite Classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/fighter.png')
        self.rect = self.image.get_rect(center=window.center)
        self.speed = 0
        self.vector = pygame.Vector2(0, 0)

    def update(self):
        self.vector.y = self.speed * -1
        self.rect.move_ip(self.vector)
        # check if off screen
        if self.rect.bottom < 0:
            self.rect.top = window.bottom
        
    def move(self):
        self.speed = 5

    def stop(self):
        if self.speed > 0:
            self.speed *= .98


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

    all_sprites.update()

    screen.fill('black')

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
