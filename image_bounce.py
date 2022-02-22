import pygame
import os
pygame.init()

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()


path = os.getcwd()

# pygame support BMP, PNG, JPG, and GIF
# returns a Surface object
beach_img = pygame.image.load(os.path.join(path, 'media/beach.jpg')).convert()
beach_rect = beach_img.get_rect()

ball_img = pygame.image.load(os.path.join(path, 'media/beachball.gif')).convert_alpha()
# ball_img = pygame.transform.scale(ball_img, (ball_img.get_width()//2, ball_img.get_height()//2))
ball = ball_img.get_rect(center = window.center) # returns a Rect object
# .get_rect() defaults to (0, 0)
# .get_rect(center=(100, 100)) you can change the starting location with center argument


velocity = pygame.Vector2(10, 5)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rect objects have a built-in move method
    # ball = ball.move(speed) # returns a new Rect object in new location
    ball.move_ip(velocity) # just moves the currect Rect object

    if ball.left < 0 or ball.right > screen.get_width():
        velocity.x *= -1
    
    if ball.top < 0 or ball.bottom > screen.get_height():
        velocity.y *= -1

    screen.fill('white')
    screen.blit(beach_img, beach_rect)
    screen.blit(ball_img, ball)
    pygame.display.flip()

pygame.quit()
