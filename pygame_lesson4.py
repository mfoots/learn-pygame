import pygame
import os

pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()

def end_game():
    pygame.quit()
    quit()

class Laser(pygame.sprite.Sprite):
    def __init__(self, parent):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'laserRed.png')).convert_alpha()
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
        self.image = pygame.image.load(os.path.join('assets', 'player.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = window.centerx
        self.rect.bottom = window.bottom - 15
        self.vector = pygame.Vector2(0,0)

    def update(self):
        self.rect.move_ip(self.vector)

    def fire(self):
        laser = Laser(self)
        laser_sprites.add(laser)
        all_sprites.add(laser)


player1 = Player()
all_sprites = pygame.sprite.RenderUpdates()
all_sprites.add(player1)

laser_sprites = pygame.sprite.RenderUpdates()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end_game()
            if event.key == pygame.K_SPACE:
                player1.fire()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player1.vector = 5,0
    if keys[pygame.K_LEFT]:
        player1.vector = -5,0


    if player1.rect.left < 0:
        player1.rect.left = 0
    if player1.rect.right > window.width:
        player1.rect.right = window.right

    
    all_sprites.update()


    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
    