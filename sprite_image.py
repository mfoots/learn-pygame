import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()

# Define Sprite Classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('assets/bsg-ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=window.center)

# Create Sprite Objects
ship = Ship()

# Sprite Groups
all_sprites = pygame.sprite.RenderUpdates()
all_sprites.add(ship)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
