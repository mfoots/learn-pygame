import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()

box = pygame.Rect(0, 0, 50, 50)
box.center = window.center

speed = 5
vector = pygame.Vector2(0, 0)
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                vector[1] = -speed
            if event.key == pygame.K_DOWN:
                vector[1] = speed
            if event.key == pygame.K_LEFT:
                vector[0] = -speed
            if event.key == pygame.K_RIGHT:
                vector[0] = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                vector[1] = 0
            if event.key == pygame.K_DOWN:
                vector[1] = 0
            if event.key == pygame.K_LEFT:
                vector[0] = 0
            if event.key == pygame.K_RIGHT:
                vector[0] = 0

    box.move_ip(vector)
    if box.left > window.right:
        box.right = 0
    if box.right < 0:
        box.left = window.right
    if box.bottom < 0:
        box.top = window.bottom
    if box.top > window.bottom:
        box.bottom = 0

    screen.fill('mintcream')
    pygame.draw.rect(screen, 'tomato', box )
    pygame.display.flip()

pygame.quit()
