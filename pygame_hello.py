import pygame, sys
pygame.init()
SCREEN_SIZE = 400, 400
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Hello, Pygame")
window = screen.get_rect()

fps_clock = pygame.time.Clock()
FPS = 60
BACKGROUND = 0, 0, 0

# default_font = pygame.font.get_default_font()
# all_fonts = pygame.font.get_fonts()

font = pygame.font.SysFont('monospace', 32)
text = font.render('Welcome to Pygame', True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = window.center

def start():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(BACKGROUND)

        screen.blit(text, text_rect)

        pygame.display.update()
        fps_clock.tick(FPS)

start()