import sys
import pygame

SCREEN_SIZE = (640, 480)
SPEED = 3
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize the pygame modules
pygame.init()
pygame.display.set_caption("Image Blit Example")

# create the main display surface
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

class GameObject:
    def __init__(self, image, speed):
        self.speed = speed
        self.image = pygame.transform.rotate(image, -90)
        self.pos = image.get_rect().move(screen_rect.centerx, screen_rect.centery)

    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > screen_rect.right:
            self.pos.left = 0

    def rotate(self):
        pass

background = pygame.image.load('media/starfield_bg.png').convert()
player_image = pygame.image.load('media/ship.png').convert_alpha()


player = GameObject(player_image, 2)
screen.blit(background, (0, 0))

# game loop
while True:
    # loop through all the events
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
                quit()

    screen.blit(background, player.pos, player.pos)
    player.move()
    screen.blit(player.image, player.pos)

    pygame.display.update()
    clock.tick(FPS)
