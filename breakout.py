import random
import pygame

BRICK_WIDTH = 64
BRICK_HEIGHT = 15
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
BRICK_COLORS = [RED, ORANGE, GREEN, YELLOW]

pygame.init()
screen = pygame.display.set_mode((640,480))
window = screen.get_rect()
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()

def terminate():
    pygame.quit()
    quit()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((100, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center = (window.centerx, window.height - 20))
        self.vector = pygame.Vector2(0,0)
        self.score = Scoreboard(all_sprites)

    def update(self):
        self.rect.move_ip(self.vector)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vector.x = -10
        elif keys[pygame.K_RIGHT]:
            self.vector.x = 10
        else:
            self.vector.x = 0

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window.width:
            self.rect.right = window.width

class Ball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, WHITE, self.rect.center, 10)
        self.rect.center = window.center
        self.vector = pygame.Vector2(0,0)
        self.set_vector()

    def set_vector(self):
        x = random.choice([random.randint(-6, -4), random.randint(4, 6)])
        if self.vector.y > 0:
            y = random.randint(-6, -4)
        elif self.vector.y <= 0:
            y = random.randint(4, 6)

        self.vector = pygame.Vector2(x, y)

    def update(self):
        hits = pygame.sprite.spritecollide(self, brick_sprites, False)  # correction
        if hits:
            for hit in hits:  
                player.score.change()
                hit.kill()
            self.set_vector()
        
        if self.rect.left <= 0:
            self.rect.left = 2   # correction
            self.vector.x *= -1
        if self.rect.right >= window.width:
            self.rect.right = window.width - 2  # correction
            self.vector.x *= -1
        if self.rect.top <= 0:
            self.rect.top = 2  # correction
            self.set_vector()

        if pygame.sprite.collide_rect(self, player):
            if self.rect.bottom >= player.rect.bottom:  # correction
                self.rect.bottom = player.rect.top - 2  # correction
                self.set_vector()
                if player.vector.x > 0:
                    self.vector.x = abs(self.vector.x)
                else:
                    self.vector.x = -abs(self.vector.x)

        self.rect.move_ip(self.vector)


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, pygame.Rect(1, 1, self.rect.width-1, self.rect.height-1))
        self.rect.x = x
        self.rect.y = y

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.score = 0
        self.font = pygame.font.Font(None, 30)
        self.render_text()
        
    def change(self, n=1):
        self.score += n
        self.render_text()

    def render_text(self):
        self.image = self.font.render(f"Score: {self.score}", True, WHITE)
        self.rect = self.image.get_rect(midleft=(20, 20))

def generate_blocks():
    color_index = 0
    start = BRICK_HEIGHT + 30
    end = start + (BRICK_HEIGHT * 9 - BRICK_HEIGHT)
    for row in range(start, end, BRICK_HEIGHT):
        for column in range(0, BRICK_WIDTH * window.width//BRICK_WIDTH, BRICK_WIDTH):
            Brick(column, row, BRICK_COLORS[color_index], all_sprites, brick_sprites)
        if row % 10 == 0 and color_index < len(BRICK_COLORS) - 1:
            color_index += 1

player = Paddle(all_sprites)
ball = Ball(all_sprites)
generate_blocks()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
