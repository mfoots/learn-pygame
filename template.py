import pygame
pygame.init()

screen_size = (500, 500)
bg="#8dfafc"
screen = pygame.display.set_mode(screen_size)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg)

    pygame.display.flip()

pygame.quit()