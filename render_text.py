import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello, Pygame")
window = screen.get_rect()

clock = pygame.time.Clock()

font = pygame.font.Font(pygame.font.get_default_font(), 32)
text = font.render('Welcome to Pygame', True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = window.center


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    screen.fill((0, 150, 200))

    screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)

