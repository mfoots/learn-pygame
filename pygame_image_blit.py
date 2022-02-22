import pygame
import os
pygame.init()

# create the screen surface
screen = pygame.display.set_mode((500,500))
window = screen.get_rect()

path = os.getcwd()
bg_img = pygame.image.load(os.path.join(path, 'media/space-stars.jpg')).convert()
bg_rect = bg_img.get_rect(center = window.center)

ship_img = pygame.image.load(os.path.join(path, 'media/bsg-ship.png')).convert_alpha()
# ship_img = pygame.transform.flip(ship_img, 1, 1)
# ship_img = pygame.transform.scale(ship_img, (ship_img.get_width()//2, ship_img.get_height()//2))
ship = ship_img.get_rect(center = window.center)

running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    
    # blit draws an image surface to the screen surface
    screen.blit(bg_img, bg_rect)
    screen.blit(ship_img, ship)
    pygame.display.flip()

pygame.quit()