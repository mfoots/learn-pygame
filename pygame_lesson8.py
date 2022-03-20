import pygame
pygame.init()

FPS = 60
FRICTION = -0.12
ACCELERATION_RATE = 0.6
SKY_COLOR = (0, 120, 200)
PLAYER_COLOR = (200, 0, 50)
GROUND_COLOR = (0, 200, 60)
GROUND_HEIGHT = 80

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.position = pygame.Vector2(*self.rect.midbottom)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

    def move(self):
        '''move the sprite'''
        self.acceleration = pygame.Vector2(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -ACCELERATION_RATE
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = ACCELERATION_RATE

        self.acceleration.x += self.velocity.x * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        if self.position.x < 0:
            self.position.x = window.width
        if self.position.x > window.width:
            self.position.x = 0
    
    def jump(self):
        '''control jumping'''
        if pygame.sprite.spritecollide(self, obstacles, False):
            self.velocity.y = -15

    def update(self):
        '''move the sprite then check for collitions'''
        self.move()
        
        hits = pygame.sprite.spritecollide(self, obstacles, False)
        if self.velocity.y > 0:
            if hits:
                self.velocity.y = 0
                self.position.y = hits[0].rect.top + 1

        

        self.rect.midbottom = self.position
                

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
all_sprites = pygame.sprite.RenderUpdates()
obstacles = pygame.sprite.RenderUpdates()

player1 = Player(PLAYER_COLOR, window.centerx, window.centery, 50, 50)
player1.add(all_sprites)
ground = Platform(GROUND_COLOR, 0, window.height - GROUND_HEIGHT, window.width, GROUND_HEIGHT)
ground.add(all_sprites, obstacles)


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
                player1.jump()

                
    all_sprites.update()
    screen.fill(SKY_COLOR)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
