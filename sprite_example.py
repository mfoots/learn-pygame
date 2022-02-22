import sys
import os
import math
import pygame
import random

SCREEN_SIZE = (640, 480)

# initialize the pygame modules
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screenrect = screen.get_rect()
pygame.display.set_caption("Sprite Example")
clock = pygame.time.Clock()
path, filename = os.path.split(os.path.realpath(__file__))

allsprites = pygame.sprite.LayeredUpdates()
rocks = pygame.sprite.LayeredUpdates()

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(os.path.join(path, 'assets/ship.png')).convert_alpha()
        self.image = self.original_image
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Vector2(screen.get_rect().center)
        self.angle = 0
        self.pivot = [self.rect.centerx, self.rect.centery]
        self.offset = pygame.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 0

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.pivot + self.offset.rotate(self.angle))
        self.angle = self.angle % 360

    def move(self):
        self.speed = 5
         
    def update(self):
        self.dx += self.speed * math.sin(math.radians(self.angle)) * -1
        self.dy += self.speed * math.cos(math.radians(self.angle)) * -1
        self.rect.center += pygame.Vector2(self.dx, self.dy)
        self.speed *= .97   

        if self.rect.centerx < 0:
            self.rect.move_ip(screen.get_rect().width, 0)
            self.dx += screen.get_rect().width

        if self.rect.centerx > screen.get_rect().width:
            self.rect.move_ip(-screen.get_rect().width, 0)
            self.dx += -screen.get_rect().width

        if self.rect.centery < 0:
            self.rect.move_ip(0, screen.get_rect().height)
            self.dy += screen.get_rect().height

        if self.rect.centery > screen.get_rect().height:
            self.rect.move_ip(0, -screen.get_rect().height)
            self.dy += -screen.get_rect().height

    def fire(self):
        bullet = Bullet(self)
        allsprites.add(bullet, layer=0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, origin):
        pygame.sprite.Sprite.__init__(self)
        self.origin = origin
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.origin.rect.center
        self.angle = self.origin.angle
        self.dx = 0
        self.dy = 0
        self.speed = 5

    def update(self):
        self.angle = self.origin.angle
        self.dx += self.speed * math.sin(math.radians(self.angle)) * -1
        self.dy += self.speed * math.cos(math.radians(self.angle)) * -1
        self.rect.center += pygame.Vector2(self.dx, self.dy)

        collisions = pygame.sprite.spritecollide(self, rocks, True)
        if collisions:
            rock = Rock()
            allsprites.add(rock, layer=1)
            rocks.add(rock, layer=1)
            


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(path, 'assets/meteor.png')).convert_alpha()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(1, screenrect.width - self.rect.width)
        self.rect.top = random.randint(1, screenrect.height - self.rect.height)


background = pygame.image.load(os.path.join(path, 'assets/starfield_bg.png')).convert()

ship = Ship()
rock = Rock()
allsprites.add(ship, layer=1)
allsprites.add(rock, layer=1)
rocks.add(rock, layer=1)

# game loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
                quit()
    
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.angle += 5
    if keys[pygame.K_RIGHT]:
        ship.angle -= 5
    if keys[pygame.K_UP]:
        ship.move()
    if keys[pygame.K_SPACE]:
        ship.fire()
    
    # collisions = pygame.sprite.spritecollide(ship, rocks)
        
    
    ship.rotate()
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.update()
