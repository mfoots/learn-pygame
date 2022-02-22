import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
window = screen.get_rect()
clock = pygame.time.Clock()

# STEP TWO: Create one or more sprite groups
all_the_sprites = pygame.sprite.RenderUpdates()
target_sprites = pygame.sprite.RenderUpdates()

# STEP ONE: Define both sprite classes
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        '''the initializing method'''
        super().__init__() 
        self.image = pygame.Surface((50, 50)) 
        self.image.fill('green') 
        self.rect = self.image.get_rect() 
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        # STEP SEVEN: Check for collisions with sprite group
        for sprite in pygame.sprite.spritecollide(self, target_sprites, 0):
            sprite.move()

class Target(pygame.sprite.Sprite):
    def __init__(self):
        '''the initializing method'''
        super().__init__() 
        self.image = pygame.Surface((50, 50)) 
        self.image.fill('red') 
        self.rect = self.image.get_rect()
        self.move() # sets the initial random position

    def move(self):
        '''move the sprite to a random location'''
        x = random.randrange(window.width - 50)
        y = random.randrange(window.height - 50)
        self.rect.center = (x, y)

# STEP THREE: Create some sprite obejcts
my_sprite = MySprite()
target1 = Target()
target2 = Target()

# STEP FOUR: Add each sprite to one or more sprite groups
all_the_sprites.add(my_sprite)
all_the_sprites.add(target1)
all_the_sprites.add(target2)
target_sprites.add(target1)
target_sprites.add(target2)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False


    # STEP SIX: Call all the sprites update methods
    all_the_sprites.update()

    screen.fill('black')

    # STEP FIVE: Draw all of your sprites to the screen
    all_the_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
