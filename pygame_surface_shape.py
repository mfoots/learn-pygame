import pygame
import os
pygame.init()

WINDOW_SIZE = (500, 500)
BG = pygame.Color(0, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)
window = screen.get_rect()

image = pygame.Surface((30, 30))
image_rect = image.get_rect(center=window.center)
points = (
    (image_rect.centerx,image_rect.top),
    (image_rect.left,image_rect.bottom),
    (image_rect.right,image_rect.bottom)
)
# pygame.draw.polygon(image, (255,255,255), points, 1)
# screen.blit(image, image_rect)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BG)
    
    pygame.draw.polygon(image, (255,255,255), points, 1)
    screen.blit(image, image_rect)
    

    pygame.display.update()

pygame.quit()