import sys
import os
import random
from turtle import window_width
import pygame

# CONSTANTS

BRICK_WIDTH = 64
BRICK_HEIGHT = 15
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARKGRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

# initialize stuff
pygame.init()
screen = pygame.display.set_mode((640,480))
window = screen.get_rect()
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

def terminate():
    pygame.quit()
    quit()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((100, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center = (window.centerx, window.height - 20))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 10

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window.width:
            self.rect.right = window.width

class Ball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, WHITE, self.rect.center, 10)
        self.vector = pygame.Vector2(self.set_vector())
        self.rect.center = window.center

    def set_vector(self):
        x = random.choice([random.randint(-5, -3), random.randint(3, 5)])
        y = random.randint(3, 5)
        return pygame.Vector2(x, y)

    def update(self):
        self.rect.move_ip(self.vector)
        
        if self.rect.left < 0 or self.rect.right > window.width:
            self.vector.x *= -1
        if self.rect.top < 0:
            self.vector.y *= -1

        if pygame.sprite.collide_rect(self, player):
            self.vector = self.set_vector()
            self.vector.y *= -1


player = Paddle(all_sprites)
ball = Ball(all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
