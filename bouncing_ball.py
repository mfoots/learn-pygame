import sys
import pygame

SCREEN_SIZE = 320, 240

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen_rect = screen.get_rect()
pygame.display.set_caption("Boucing Ball")
clock = pygame.time.Clock()

ball = pygame.Rect(screen_rect.centerx - 10, screen_rect.centery - 10, 10, 10)

x_velocity = 1
y_velocity = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    screen.fill(BLACK)

    ball.x += x_velocity
    ball.y += y_velocity

    if ball.left < 0:
        ball.left = 0
        x_velocity = -x_velocity
        
    if ball.right > screen_rect.w:
        ball.right = screen_rect.w
        x_velocity = -x_velocity
    
    if ball.top < 0:
        ball.top = 0
        y_velocity = -y_velocity
    
    if ball.bottom > screen_rect.h:
        ball.bottom = screen_rect.h
        y_velocity = -y_velocity


    pygame.draw.circle(screen, GREEN, ball.center, 10)
    
    pygame.display.update()
    clock.tick(60)
