import pygame, random
pygame.init()

BLOCKSIZE = 30
BACKGROUND = (50, 50, 50)
PLAYER_COLOR = (100, 200, 50)
TARGET_COLOR = (200, 0, 50)
FPS = 10
SPEED = BLOCKSIZE

screen = pygame.display.set_mode((BLOCKSIZE*20, BLOCKSIZE*15))
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

print(window.size)

class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = BLOCKSIZE
        self.rect.y = BLOCKSIZE
        self.set_location()
        self.add(all_sprites)
        self.vector = pygame.Vector2(0,0)

    def set_location(self):
        self.rect.x = BLOCKSIZE * random.randint(1, window.width//BLOCKSIZE - 1)
        self.rect.y = BLOCKSIZE * random.randint(1, window.height//BLOCKSIZE - 1)

class Player(Block):
    def __init__(self, color):
        super().__init__(color)
        self.score = Scoreboard()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vector = -SPEED, 0
        if keys[pygame.K_RIGHT]:
            self.vector = SPEED, 0
        if keys[pygame.K_UP]:
            self.vector = 0, -SPEED
        if keys[pygame.K_DOWN]:
            self.vector = 0, SPEED

        if self.rect.right > window.width:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = window.width

        if self.rect.bottom > window.height:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = window.height

        self.rect.move_ip(self.vector)

        if pygame.sprite.collide_rect(self, target):
            self.score.change(1)

class Target(Block):
    
    def update(self):
        if pygame.sprite.collide_rect(self, player):
            self.set_location()


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 30)
        self.score = 0
        self.add(all_sprites)
        self.display()

    def change(self, amount):
        self.score += amount

    def display(self):
        self.image = self.font.render(f"{self.score}", True, (255,255,255))
        self.rect = self.image.get_rect(midtop=(window.centerx, 10))

    def update(self):
        self.display()


target = Target(TARGET_COLOR)
player = Player(PLAYER_COLOR)

def draw_grid():
    # vertical lines
    for i in range(window.width//BLOCKSIZE):
        x = BLOCKSIZE * i
        pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, window.height))

    # horizontal lines
    for i in range(window.height//BLOCKSIZE):
        y = BLOCKSIZE * i
        pygame.draw.line(screen, (100, 100, 100), (0, y), (window.width, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN\
        and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

    all_sprites.update()
    screen.fill(BACKGROUND)
    draw_grid()
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
