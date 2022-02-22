import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()

dot = pygame.Rect(0, 0, 50, 50)
dot.center = (window.centerx, window.centery)
dot_color = pygame.Color(0, 255, 255)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            dot_color = pygame.Color(255, 255, 0)
        if event.type == pygame.MOUSEBUTTONUP:
            dot_color = pygame.Color(0, 255, 255)


    dot.center = pygame.mouse.get_pos()

    screen.fill('honeydew')

    pygame.draw.ellipse(screen, dot_color, dot)

    pygame.display.flip()

pygame.quit()