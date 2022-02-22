import sys
import pygame

pygame.init()

BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
SCREEN_SIZE = (400, 200)
BLOCK_SIZE = 25

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Moving Box")
clock = pygame.time.Clock()

box = pygame.Rect(0, 100, BLOCK_SIZE, BLOCK_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            quit()

    screen.fill(CYAN)

    if box.x < SCREEN_SIZE[0]:
        box.x += 1
    else:
        box.x = 0
    pygame.draw.rect(screen, BLACK, box)

    pygame.display.update()
    clock.tick(60)
