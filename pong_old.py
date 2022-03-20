import pygame
from random import randint
import os
pygame.init()


screen = pygame.display.set_mode((500,600))
window = screen.get_rect()

paddle = pygame.Rect(window.right - 20, 0, 10, 100)

ball = pygame.Rect(randint(0, window.width//2), randint(0, window.height//2), 25, 25)
ball_vect = pygame.Vector2([5,5])

path = os.getcwd()
ping = pygame.mixer.Sound(os.path.join(path, 'media/pong_high.wav'))
pong = pygame.mixer.Sound(os.path.join(path, 'media/pong_low.wav'))
game_over_sound = pygame.mixer.Sound(os.path.join(path, 'media/game_over.wav'))

go_font = pygame.font.Font(None, 60)
go_surface = go_font.render('Game Over!', False, (0, 255, 0))
go_rect = go_surface.get_rect(center=window.center)

score = 0

score_font = pygame.font.Font(None, 60)
score_surface = score_font.render(str(score), False, 'white')
score_rect = score_surface.get_rect(center=(window.centerx, 40))

clock = pygame.time.Clock()

game_over = False

running = True
while running:
    pygame.mouse.set_visible(0)
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle.centery = pygame.mouse.get_pos()[1]
    ball.move_ip(ball_vect)
    if ball.left < 0:
        ball_vect[0] *= -1
        pong.play()

    if ball.top < 0 or ball.bottom > window.height:
        ball_vect[1] *= -1
        pong.play()

    if pygame.Rect.colliderect(paddle, ball):
        score += 1
        ball.x -= 25
        ball_vect[0] *= -1
        ping.play()

    if ball.right > window.right:
        ball_vect = [0,0]
        ball.center = window.center
        game_over = True
        game_over_sound.play()


    screen.fill('black')
    score_surface = score_font.render(str(score), False, 'white')
    if not game_over:
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        pygame.draw.rect(screen, (255, 255, 255), paddle)
    else:
        screen.blit(go_surface, go_rect)
    
    screen.blit(score_surface, score_rect)

    
    pygame.display.flip()

pygame.quit()
