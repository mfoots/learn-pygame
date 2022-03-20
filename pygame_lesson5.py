import pygame, random
pygame.init()

DOT_SIZE = 10
FPS = 60
BACKGROUND = (0, 120, 200)
COLORS = [
    (180, 0, 60),
    (180, 200, 0),
    (0, 180, 50),
    (150, 0, 200),
    (200, 150, 0),
    (0, 60, 200),
]

screen = pygame.display.set_mode((400, 400))
window = screen.get_rect()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
all_sprites = pygame.sprite.Group()
dots = pygame.sprite.Group()

class Dot(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(BACKGROUND)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, color, self.rect.center, DOT_SIZE)
        self.rect.center = pygame.mouse.get_pos()
        self.image.set_colorkey(BACKGROUND)

class Player(Dot):
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def stamp(self):
        dot = Dot(random.choice(COLORS))
        dot.add(all_sprites, dots)

player1 = Player(COLORS[0])
player1.add(all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                player1.stamp()
            if pygame.mouse.get_pressed()[2]:
                for sprite in dots.sprites():
                    sprite.kill()
        
    all_sprites.update()

    screen.fill(BACKGROUND)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)