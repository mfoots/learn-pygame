import pygame
pygame.init()

WINDOW_SIZE = (500, 500)
BG = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode(WINDOW_SIZE)
window = screen.get_rect()

player = pygame.Rect(*(window.center), 25, 25)
obstacle = pygame.Rect(100, 100, 25, 25)

clock = pygame.time.Clock()
vec = pygame.Vector2([0,0])
delta = 3

running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                vec = [-delta, 0]
            if keys[pygame.K_RIGHT]:
                vec = [delta, 0]
            if keys[pygame.K_UP]:
                vec = [0, -delta]
            if keys[pygame.K_DOWN]:
                vec = [0, delta]
        if event.type == pygame.KEYUP:
            vec = [0, 0]

    player.move_ip(vec)

    if pygame.Rect.colliderect(player, obstacle):
        if vec.x < 0:
            obstacle.centerx = player.centerx - player.width
        if vec.x > 0:
            obstacle.centerx = player.centerx + player.width
        if vec.y < 0:
            obstacle.centery = player.centery - player.height
        if vec.y > 0:
            obstacle.centery = player.centery + player.height
        print(obstacle.center)

    screen.fill(BG)

    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), obstacle)
    pygame.display.flip()

pygame.quit()