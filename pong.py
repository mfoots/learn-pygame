import pygame, random
pygame.init()
pygame.mouse.set_visible(False)

FPS = 60
BACKGROUND = (0, 0, 0)
FOREGROUND = (255, 255, 255)
ASPECT_RATIOS = {
    'small': (320, 240),
    'medium': (640, 480),
    'large': (800, 600),
}

def game_over():
    pygame.quit()
    quit()

pygame.display.set_caption('PONG')
screen = pygame.display.set_mode(ASPECT_RATIOS['medium'], pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()
SIZE = window.width*0.05

all_sprites = pygame.sprite.Group()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill(BACKGROUND)
        self.image.set_colorkey(BACKGROUND)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, FOREGROUND, self.rect.center, SIZE*0.4)
        self.rect.center = window.center
        self.vector = self.set()
        self.score = Scoreboard(-50)
        self.score.add(all_sprites)

    def set(self):
        return pygame.Vector2(random.randint(3,5), random.randint(6,8))

    def update(self):
        self.rect.move_ip(self.vector)

        if self.rect.left < 0:
            self.vector.x = -self.vector.x
        if self.rect.top < 0:
            self.vector.y = -self.vector.y
        if self.rect.bottom > window.height:
            self.vector.y = -self.vector.y

        if self.rect.right > window.right:
            self.rect.center = window.center
            self.vector = self.set()
            self.score.increase(1)

        if pygame.sprite.collide_rect(self, paddle):
            self.vector = -self.vector


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SIZE*0.4, SIZE*3))
        self.image.fill(BACKGROUND)
        self.image.set_colorkey(BACKGROUND)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, FOREGROUND, pygame.Rect(0, 0, self.rect.width, self.rect.height))
        self.rect.centery = window.centery
        self.rect.right = window.right - 6
        self.score = Scoreboard(50)
        self.score.add(all_sprites)
        
    def update(self):
        self.rect.centery = pygame.mouse.get_pos()[1]

        if pygame.sprite.collide_rect(self, ball):
            self.score.increase(1)
        

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, offset):
        super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None, 50)
        self.offset = offset
        self.render_text()
        
    def increase(self, score):
        self.score += score
        self.render_text()

    def render_text(self):
        self.image = self.font.render(f'{self.score}', True, FOREGROUND)
        self.rect = self.image.get_rect(center=(window.width / 2 + self.offset, 50))


paddle = Paddle()
paddle.add(all_sprites)
ball = Ball()
ball.add(all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over()

    all_sprites.update()

    screen.fill(BACKGROUND)
    pygame.draw.line(screen, FOREGROUND, (window.width*0.5, 0), (window.width*0.5, window.height), 1)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
