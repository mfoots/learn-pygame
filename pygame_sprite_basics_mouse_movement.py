import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,600))
window = screen.get_rect()
clock = pygame.time.Clock()

# STEP TWO: Create one or more sprite groups
all_the_sprites = pygame.sprite.RenderUpdates()

# STEP ONE: Define your sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        '''the initializing method'''
        super().__init__() # pull in the Sprite class init
        self.image = pygame.Surface((50, 50)) # you could also load an image
        self.image.fill('green') # fill it with a color
        self.rect = self.image.get_rect() # retangular reference to Surface
        # set the sprites initial location to the mouse pointer location
        self.rect.center = pygame.mouse.get_pos()
        

    # STEP SIX: Define you update method
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

# STEP THREE: Create a sprite object
my_sprite = MySprite()

# STEP FOUR: Add your sprite to one or more sprite groups
all_the_sprites.add(my_sprite)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    # STEP SEVEN: Call all the sprites update methods
    all_the_sprites.update()

    screen.fill('black')

    # STEP FIVE: Draw all of your sprites to the screen
    all_the_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
