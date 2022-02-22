import sys
import pygame
from pygame.constants import K_LEFT

SCREEN_SIZE = (640, 480)
SHIP_SIZE = 30
SPEED = 3
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
window = screen.get_rect()
pygame.display.set_caption("Movement")
clock = pygame.time.Clock()

class Ship(pygame.sprite.Sprite):
    def __init__(self, size=30):
        super(Ship, self).__init__()
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center = window.center)
        self.pointlist = [(self.rect.left, self.rect.bottom),
                          (self.rect.left + 5, self.rect.bottom - 5),
                          (self.rect.right - 5, self.rect.bottom - 5),
                          (self.rect.right, self.rect.bottom),
                          (self.rect.centerx, self.rect.top)]
        self.bounds = pygame.draw.polygon(self.surf, WHITE, self.pointlist, 1)

    def draw(self):
        pygame.draw.polygon(self.surf, WHITE, self.pointlist, 1)
        screen.blit(self.surf, self.bounds)

    def update(self, keys_pressed):
        if keys_pressed[K_LEFT]:
            pygame.transform.rotate(self.surf, 45)
        self.draw()

ship = Ship()

while True:

    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
                quit()

    keys_pressed = pygame.key.get_pressed()

    screen.fill(BLACK)

    ship.update(keys_pressed)
    # ship.draw()
    # screen.blit(ship.surf, ship.rect)

    pygame.display.flip()
    clock.tick(FPS)
