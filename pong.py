import pygame, random
pygame.init()

FPS = 60
BACKGROUND = (0, 0, 0)
FOREGROUND = (255, 255, 255)

screen = pygame.display.set_mode((800,600))
window = screen.get_rect()
clock = pygame.time.Clock()
ping = pygame.mixer.Sound('assets/pong_high.wav')
pong = pygame.mixer.Sound('assets/pong_low.wav')

all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BACKGROUND)
        self.image.set_colorkey(BACKGROUND)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, FOREGROUND, self.rect.center, 10)
        self.rect.center = window.center
        self.vector = self.set()

    def set(self):
        return pygame.Vector2(random.randint(3,5), random.choice([random.randint(6,8),random.randint(-8,-6)]))

    def update(self):
        self.rect.move_ip(self.vector)

        if self.rect.top <= 2:
            self.vector.y = -self.vector.y
            ping.play()

        if self.rect.y >= window.height - self.rect.height :
            self.vector.y = -self.vector.y
            ping.play()

        if self.rect.left < 0:
            self.rect.center = window.center
            self.vector = self.set()
            player.score.increase(1)

        if self.rect.right > window.right:
            self.rect.center = window.center
            self.vector = self.set()
            computer.score.increase(1)

        if pygame.sprite.spritecollide(self, paddles, False):
            self.vector = -self.vector
            self.vector.y = random.choice([self.vector.y, -self.vector.y])
            self.vector = self.vector * 1.1
            pong.play()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill(BACKGROUND)
        self.image.set_colorkey(BACKGROUND)
        self.rect = self.image.get_rect(center=(x,y))
        pygame.draw.rect(self.image, FOREGROUND, pygame.Rect(0, 0, self.rect.width, self.rect.height))

    def check_bounds(self):
        if self.rect.top <= 0:
                self.rect.top = 0
        if self.rect.bottom >= window.height:
            self.rect.bottom = window.height

class Player(Paddle):
    def __init__(self, x, y):
        Paddle.__init__(self, x, y)
        self.score = Scoreboard(50)
        self.score.add(all_sprites)

    def update(self):
        self.rect.centery = pygame.mouse.get_pos()[1]
        self.check_bounds()

class Computer(Paddle):
    def __init__(self, x, y):
        Paddle.__init__(self, x, y)
        self.score = Scoreboard(-50)
        self.score.add(all_sprites)

    def update(self):
        if ball.rect.x < window.centerx:
            if ball.vector.y < 0:
                self.rect.y -= abs(ball.vector.y/2)
            if ball.vector.y > 0:
                self.rect.y += abs(ball.vector.y/2)
        self.check_bounds()

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

computer = Computer(window.left + 10, window.centery)
computer.add(all_sprites, paddles)

player = Player(window.right - 10, window.centery)
player.add(all_sprites, paddles)

ball = Ball()
ball.add(all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

    all_sprites.update()

    screen.fill(BACKGROUND)
    pygame.draw.line(screen, FOREGROUND, (window.width*0.5, 0), (window.width*0.5, window.height), 1)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
