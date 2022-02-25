import pygame
import time

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((480, 240))

    ball = pygame.image.load('assets/ball.png')
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.process_time()
            frame_rate = 500 / (t1 - t0)
            t0 = t1

        main_surface.fill((0, 200, 255))

        main_surface.fill((255, 0, 0), (300, 100, 150, 90))

        main_surface.blit(ball, (50, 70))

        the_text = my_font.render(f"Frame = {frame_count}, rate = {frame_rate:0.2f} fps", True, (0, 0, 0))
        main_surface.blit(the_text, (10, 10))

        pygame.display.flip()
        
    pygame.quit()

main()