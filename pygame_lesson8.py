import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.RenderUpdates()
laser_sprites = pygame.sprite.RenderUpdates()
meteor_sprites = pygame.sprite.RenderUpdates()

def end_game():
    pygame.quit()
    quit()

meteor_image_big = pygame.image.load('assets/spaceArt/png/meteorBig.png').convert_alpha()
meteor_image_small = pygame.image.load('assets/spaceArt/png/meteorSmall.png').convert_alpha()
laser_red_image = pygame.image.load('assets/spaceArt/png/laserRed.png').convert_alpha()
laser_red_shot_image = pygame.image.load('assets/spaceArt/png/laserRedShot.png').convert_alpha()
player_image = pygame.image.load('assets/spaceArt/png/player.png').convert_alpha()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = meteor_image_big
        self.rect = self.image.get_rect(center=(x,y))
        self.vector = pygame.Vector2(1,0)

    def update(self):
        self.rect.move_ip(self.vector)

class Laser(pygame.sprite.Sprite):
    def __init__(self, parent):
        super().__init__()
        self.image = laser_red_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = parent.rect.midtop
        self.vector = pygame.Vector2(0,-10)
        self.time_of_hit = 0

    def update(self):
        self.rect.move_ip(self.vector)
        if self.rect.bottom < window.top:
            self.kill()

        if self.time_of_hit > 0 and pygame.time.get_ticks() > self.time_of_hit * 1.05:
            self.kill()
            self.time_of_hit = 0

        hits = pygame.sprite.spritecollide(self, meteor_sprites, True)
        if hits:
            self.image = laser_red_shot_image
            self.rect = self.image.get_rect(center=hits[0].rect.midbottom)
            self.vector = (0,0)
            self.time_of_hit = pygame.time.get_ticks()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
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
player1.add(all_sprites)

meteor1 = Meteor(100, 100)
meteor1.add(all_sprites, meteor_sprites)

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
    
    