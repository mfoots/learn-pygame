import sys
import pygame

# constants
SCREEN_SIZE = (640, 480)
SCREEN_WIDTH = SCREEN_SIZE[0]
SCREEN_HEIGHT = SCREEN_SIZE[1]
BLOCK_SIZE = 25
SPEED = 5
FPS = 60
START_X = SCREEN_SIZE[0]//2 - BLOCK_SIZE
START_Y = SCREEN_SIZE[1]//2 - BLOCK_SIZE
BACKGROUND_COLOR = (150, 100, 225)
BLOCK_COLOR = (255, 200, 0)

# initialize
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Key Commander")
clock = pygame.time.Clock()
box = pygame.Rect(START_X, START_Y, BLOCK_SIZE, BLOCK_SIZE)
delta_x = 0
delta_y = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            quit()

        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_LEFT:
                delta_y = 0
                delta_x = -SPEED
            if event.key == pygame.K_RIGHT:
                delta_y = 0
                delta_x = SPEED
            if event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -SPEED
            if event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = SPEED

        if event.type == pygame.KEYUP:
            delta_x = 0
            delta_y = 0

    screen.fill(BACKGROUND_COLOR)

    box.x += delta_x
    box.y += delta_y


    if box.left < 0:
        box.left = 0
    if box.right > SCREEN_WIDTH:
        box.right = SCREEN_WIDTH
    if box.top < 0:
        box.top = 0
    if box.bottom > SCREEN_HEIGHT:
        box.bottom = SCREEN_HEIGHT

    pygame.draw.rect(screen, BLOCK_COLOR, box)
    pygame.display.flip()
    clock.tick(FPS)
