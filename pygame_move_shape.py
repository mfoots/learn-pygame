import pygame, sys
pygame.init()

BACKGROUND = (240, 240, 255)
BORDER = (50, 50, 25)
RED = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE = (0, 0, 255)

display = pygame.display.set_mode((400,400))
window = display.get_rect()
pygame.display.set_caption("Hello Pygame")
fpsClock = pygame.time.Clock()
FPS = 100

rectangle1 = pygame.Rect(0, 50, 50, 50)
rectangle2 = pygame.Rect(0, 0, 50, 100)
rectangle2.centerx = window.centerx
rectangle2.bottom = window.bottom
frame = pygame.Rect(0, 0, 400, 400)

def gameLoop():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
            (event.type == pygame.KEYDOWN and \
             event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        display.fill(BACKGROUND)

        pygame.draw.rect(display, RED, rectangle1)
        pygame.draw.rect(display, BLUE, rectangle2)
        pygame.draw.rect(display, BORDER, frame, 10)

        rectangle1.left += 1
        if rectangle1.left > 400:
            rectangle1.right = 0

        rectangle2.top -= 1
        if rectangle2.bottom < window.top:
            rectangle2.top = window.bottom
        
        pygame.display.flip()
        fpsClock.tick(FPS)

gameLoop()
