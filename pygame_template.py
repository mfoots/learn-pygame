import pygame
pygame.init()

FPS = 60
BACKGROUND = (50, 50, 50)
FOREGROUND = (200, 100, 50)

screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
window = screen.get_width()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, FOREGROUND, pygame.Rect(100, 100, 50, 50))
    pygame.display.update()
    clock.tick(FPS)
