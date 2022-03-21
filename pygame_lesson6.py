import pygame
pygame.init()

FPS = 60
BACKGROUND = (50, 50, 50)
FOREGROUND = (200, 100, 50)
ALTCOLOR = (50, 150, 200)
FRICTION = -0.12
ACCELERATION_RATE = 0.5
BLOCK_SIZE = 50

screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x,y))
        self.mask = pygame.mask.from_surface(self.image)


class Player(Block):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.position = pygame.Vector2(*self.rect.center)
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0,0)

    def update(self):
        self.acceleration = pygame.Vector2(0, 0)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -ACCELERATION_RATE
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = ACCELERATION_RATE
        if keys[pygame.K_UP]:
            self.acceleration.y = -ACCELERATION_RATE
        if keys[pygame.K_DOWN]:
            self.acceleration.y = ACCELERATION_RATE

        self.acceleration.x += self.velocity.x * FRICTION
        self.acceleration.y += self.velocity.y * FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        self.check_for_collisions()
        self.loop()
        self.rect.center = self.position

    def loop(self):
        offset = BLOCK_SIZE*0.5
        if self.position.x < -offset:
            self.position.x = window.width + offset
        if self.position.x > window.width + offset:
            self.position.x = -offset

        if self.position.y < -offset:
            self.position.y = window.height + offset
        if self.position.y > window.height + offset:
            self.position.y = -offset

    def check_for_collisions(self):
        hits = pygame.sprite.spritecollide(self, obstacles, False)
        if hits:
            contact_point = pygame.sprite.collide_mask(self, hits[0])
            if contact_point[0] > 0:
                self.position.x -= 2
            else:
                self.position.x += 2
            self.velocity.x = 0

            if contact_point[1] > 0:
                self.position.y -= 2
            else:
                self.position.y += 2
            self.velocity.y = 0


player1 = Player(100, 100, BLOCK_SIZE, BLOCK_SIZE, FOREGROUND)
player1.add(all_sprites)

block1 = Block(200, 300, BLOCK_SIZE*2, BLOCK_SIZE*2, ALTCOLOR)
block1.add(all_sprites, obstacles)

block2 = Block(500, 300, BLOCK_SIZE*0.75, BLOCK_SIZE*3, ALTCOLOR)
block2.add(all_sprites, obstacles)

block3 = Block(400, 100, BLOCK_SIZE*5, BLOCK_SIZE, ALTCOLOR)
block3.add(all_sprites, obstacles)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

    all_sprites.update()
    screen.fill(BACKGROUND)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
