import pygame
pygame.init()

# returns a Surface object
screen = pygame.display.set_mode((500, 500))
window = screen.get_rect()

myfont = pygame.font.Font(None, 60)
textsurface = myfont.render('Hello world!', False, (0, 255, 0))
textrect = textsurface.get_rect(center=window.center)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # draw text on the surface
    screen.blit(textsurface, textrect)

    pygame.display.flip()

pygame.quit()
