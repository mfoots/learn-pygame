import sys
from math import pi
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 102, 0)

SIZE = (600, 300)

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
            quit()

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (50, 100, 50, 100), 0)

    pygame.draw.circle(screen, GREEN, (400, 200), 40)

    pygame.draw.polygon(screen, ORANGE, ((50, 280), (550, 280), (550, 20)), 3)

    pygame.draw.line(screen, PURPLE, (75, 150), (400, 200), 4)

    pygame.draw.ellipse(screen, YELLOW, (300, 10, 100, 50), 0)

    pygame.draw.rect(screen, WHITE, (445, 95, 60, 60), 1)

    pygame.draw.arc(screen, RED, (450, 100, 50, 50), pi/2, pi, 2)
    pygame.draw.arc(screen, GREEN, (450, 100, 50, 50), 0, pi/2, 2)
    pygame.draw.arc(screen, CYAN, (450, 100, 50, 50), pi, 3*pi/2, 2)
    pygame.draw.arc(screen, YELLOW, (450, 100, 50, 50), 3*pi/2, 2*pi, 2)

    pygame.display.flip()
    clock.tick(60)
