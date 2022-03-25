import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.RenderUpdates()
laser_sprites = pygame.sprite.RenderUpdates()

laser_image = pygame.image.load('assets/spaceArt/png/laserRed.png').convert_alpha()
player_image = pygame.image.load('assets/spaceArt/png/player.png').convert_alpha()


class Laser(pygame.sprite.Sprite):
    def __init__(self, parent):
        super().__init__()
        self.image = laser_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = parent.rect.midtop
        self.vector = pygame.Vector2(0,-10)

    def update(self):
        self.rect.move_ip(self.vector)
        if self.rect.bottom < window.top:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = window.centerx
        self.rect.bottom = window.bottom - 15
        self.vector = pygame.Vector2(0,0)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vector = 5,0
        if keys[pygame.K_LEFT]:
            self.vector = -5,0

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window.width:
            self.rect.right = window.right

        self.rect.move_ip(self.vector)

    def fire(self):
        laser = Laser(self)
        laser_sprites.add(laser)
        all_sprites.add(laser)


player1 = Player()
all_sprites.add(player1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                player1.fire()

    all_sprites.update()

    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
    