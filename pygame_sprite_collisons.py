import pygame
from pygame.locals import *
import math
from random import choice, randrange
pygame.init()

screen = pygame.display.set_mode((1024,768))
window = screen.get_rect()

# Define Sprite Classes
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # store the original image
        self.original_image = pygame.image.load('media/fighter.png').convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=window.center)
        self.speed = 0
        self.vector = pygame.Vector2(0, 0)
        self.angle = 0
        # store the original center point
        self.pivot = pygame.Vector2(self.rect.center)
        self.offset = pygame.Vector2(0, 0)

    def update(self):
        self.check_hits()
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

    def check_hits(self):
        global game_over
        if pygame.sprite.spritecollide(self, asteroid_sprites, 0, pygame.sprite.collide_mask):
        # if pygame.sprite.spritecollide(self, asteroid_sprites, 0):
            game_over = True

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        # readjust the center of the rectangle
        self.rect = self.image.get_rect(center=self.pivot + self.offset.rotate(self.angle)) # Why?
        self.angle = self.angle % 360

    def move(self):
        self.speed = 5

    def stop(self):
        if self.speed > 0:
            self.speed *= .98

    def fire(self):
        torpedo = Torpedo(self)
        torpedo_sprites.add(torpedo, layer=0)
        all_sprites.add(torpedo, layer=0)

class Torpedo(pygame.sprite.Sprite):
    def __init__(self, origin):
        super().__init__()
        self.origin = origin
        self.image = pygame.Surface((5, 5))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=self.origin.rect.center)
        self.angle = self.origin.angle
        self.vector = pygame.Vector2(0,0)
        self.speed = 1

    def update(self):
        self.check_hits()
        self.angle = self.origin.angle
        self.vector.x += self.speed * math.sin(math.radians(self.angle)) * -1
        self.vector.y += self.speed * math.cos(math.radians(self.angle)) * -1
        self.rect.center += self.vector

        # if self.rect.centerx < 0 or self.rect.centerx > window.width:
        #     self.kill()
        # if self.rect.centery < 0 or self.rect.centery > window.height:
        #     self.kill()

        if abs(self.origin.rect.centerx - self.rect.centerx)  > 300 or \
           abs(self.origin.rect.centery - self.rect.centery) > 300:
            self.kill()

    def check_hits(self):
        asteroid_hits = pygame.sprite.spritecollide(self, asteroid_sprites, 1)
        for asteroid in asteroid_hits:
            offset = 100
            points = [
                (asteroid.rect.centerx + offset, asteroid.rect.centery),
                (asteroid.rect.centerx, asteroid.rect.centery + offset),
                (asteroid.rect.centerx + offset, asteroid.rect.centery + offset)
            ]
            if asteroid.size == 'large':
                make_asteroid(size='medium', location=choice(points))
                make_asteroid(size='medium', location=choice(points))
            if asteroid.size == 'medium':
                make_asteroid(size='small', location=choice(points))
                make_asteroid(size='small', location=choice(points))
            asteroid.kill()
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, size='large', position=(0,0)):
        super().__init__()
        asteroids = {
            'large':'media/asteroid_large.png',
            'medium':'media/asteroid_medium.png',
            'small':'media/asteroid_small.png'
        }
        self.size = size
        self.image = pygame.image.load(asteroids[self.size]).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        vector_range = [-1, 1]
        self.vector = pygame.Vector2(choice(vector_range), choice(vector_range))
        

    def update(self):
        self.rect.move_ip(self.vector)
        if self.rect.left > window.width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = window.width
        if self.rect.top > window.height:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = window.height

# Create Sprite Objects
asteroid_sprites = pygame.sprite.LayeredUpdates()
torpedo_sprites = pygame.sprite.LayeredUpdates()
all_sprites = pygame.sprite.LayeredUpdates()
ship = Ship()
all_sprites.add(ship, layer=1)


def make_asteroid(size="large", location=(0,0)):
    asteroid = Asteroid(size, location)
    asteroid_sprites.add(asteroid, layer=1)
    all_sprites.add(asteroid, layer=1)

def load_asteroids(number=1):
    points = [
                (200, 200),
                (window.width - 200, 200),
                (100, window.height - 200),
                (window.width - 200, window.height - 200)
            ]
    for i in range(number):
        make_asteroid(size='large', location=choice(points))

load_asteroids(3)
game_over = False

# Game Over Text
game_over_font = pygame.font.Font(None, 60)
game_over_surface = game_over_font.render('Game Over', False, 'white')
game_over_rect = game_over_surface.get_rect(center=window.center)

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
    if keys[K_SPACE]:
        ship.fire()

    if not asteroid_sprites.sprites():
        load_asteroids(3)

    all_sprites.update()
    screen.fill('black')
    
    if game_over:
        screen.blit(game_over_surface, game_over_rect)
    else:
        all_sprites.draw(screen)
        for sprite in all_sprites.sprites():
                pygame.draw.rect(screen, 'red', sprite.rect, 1)
    pygame.display.flip()

pygame.quit()