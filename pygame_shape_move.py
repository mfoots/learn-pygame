import pygame
pygame.init()

# creates the main surface to draw on
screen = pygame.display.set_mode((800,600))
# screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((800,600), pygame.NOFRAME)
window = screen.get_rect()

# create a Rect object outside the Game Loop
player = pygame.Rect(0, 0, 50, 50)
# change the initial location of the Rect object
player.center = (window.centerx, window.centery)

# create a 2D Vecotor object with delta x and delta y
vec = pygame.Vector2(1,0)
# vec = pygame.Vector2(1,2)

# create a Clock object
clock = pygame.time.Clock()

# the game loop
running = True
while running:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move_ip(vec)

    if player.left > window.width:
        player.left = 0
    # if player.top > window.height:
    #     player.bottom = 0

    # make it bounce
    # if player.right > window.width:
    #     vec[0] *= -1
    # if player.left < 0:
    #     vec[0] *= -1
    # if player.bottom > window.height:
    #     vec[1] *= -1
    # if player.top < 0:
    #     vec[1] *= -1
    
    screen.fill('black')

    pygame.draw.rect(screen, 'green', player)
    pygame.display.flip()

# game loop ended
pygame.quit()