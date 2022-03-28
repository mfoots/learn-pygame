import pygame, random

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
asteroid_sprites = pygame.sprite.Group()

laser_image = pygame.image.load('assets/spaceArt/png/laserRed.png').convert_alpha()
player_image = pygame.image.load('assets/spaceArt/png/player.png').convert_alpha()
asteroid_image = {
    "small": pygame.image.load('assets/asteroid_small.png').convert_alpha(),
    "medium": pygame.image.load('assets/asteroid_medium.png').convert_alpha(),
    "large": pygame.image.load('assets/asteroid_large.png').convert_alpha(),
}
explosion_sound = pygame.mixer.Sound('assets/Explosion.wav')
laser_sound = pygame.mixer.Sound('assets/Laser.wav')

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = asteroid_image[random.choice(list(asteroid_image.keys()))]
        self.rect = self.image.get_rect(center=(x,y))
        self.velocity = pygame.Vector2(random.randint(1,4),0)

    def update(self):
        self.rect.move_ip(self.velocity)

        if self.rect.left > window.width:
            player1.score.increase(-1)
            self.rect.right = 0
        

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

        hits = pygame.sprite.spritecollide(self, asteroid_sprites, True)
        if hits:
            player1.score.increase(1)
            explosion_sound.play()
            asteroid = Asteroid(10, 200)
            asteroid.add(all_sprites, asteroid_sprites)

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self ):
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None, 50)
        self.render_text()
        
    def increase(self, score):
        self.score += score
        self.render_text()

    def render_text(self):
        self.image = self.font.render(f'{self.score}', True, (255, 255, 255))
        self.rect = self.image.get_rect(center=(window.width / 2, 50))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = window.centerx
        self.rect.bottom = window.bottom - 15
        self.vector = pygame.Vector2(0,0)
        self.score = Scoreboard()
        self.score.add(all_sprites)

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
        laser_sound.play()
        laser_sprites.add(laser)
        all_sprites.add(laser)


player1 = Player()
all_sprites.add(player1)

asteroid1 = Asteroid(10, 100)
asteroid1.add(all_sprites, asteroid_sprites)

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
    
    