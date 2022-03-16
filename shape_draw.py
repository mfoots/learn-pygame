import pygame
pygame.init()

# returns a Surface object
screen = pygame.display.set_mode((500, 500))
window = screen.get_rect()




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    screen.fill('lightblue')

    # draw a rectangle
    # pygame.draw.rect(screen, 'blue', pygame.Rect(10, 10, 75, 125))    # filled
    pygame.draw.rect(screen, 'blue', pygame.Rect(10, 10, 75, 125), 4)   # outline

    # draw a circle
    pygame.draw.circle(screen, 'red', (200,250), 50)        # filled
    # pygame.draw.circle(screen, 'red', (250,250), 50, 4)   # outline

    # draw an ellipse
    pygame.draw.ellipse(screen, 'yellow', pygame.Rect(250, 50, 200, 100))

    # draw a line
    pygame.draw.line(screen, 'orange', (50, 450), (150, 300), 5)

    # draw a polygon
    points = ((300, 300), (450, 450), (375, 300))
    pygame.draw.polygon(screen, 'purple', points)

    pygame.display.flip()

pygame.quit()
