import pygame, random, os
pygame.init()
# pygame.mouse.set_visible(False)

FPS = 60
BACKGROUND = (0, 0, 0)
FOREGROUND = (255, 255, 255)

def game_over():
    pygame.quit()
    quit()

pygame.display.set_caption('PONG')
screen = pygame.display.set_mode((640, 480), pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()
SIZE = window.width*0.05
ping = pygame.mixer.Sound(os.path.join('assets', 'pong_high.wav'))
pong = pygame.mixer.Sound(os.path.join('assets', 'pong_low.wav'))
oops = pygame.mixer.Sound(os.path.join('assets', 'ohno.wav'))


all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()

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


    def set(self):
        return pygame.Vector2(random.randint(3,5), random.randint(6,8))

    def update(self):
        self.rect.move_ip(self.vector)

        if self.rect.top <= 0:
            self.vector.y = -self.vector.y
            ping.play()

        if self.rect.y >= window.height - self.rect.height :
            self.vector.y = -self.vector.y
            ping.play()

        if self.rect.left < 0:
            self.rect.center = window.center
            self.vector = self.set()
            player.score.increase(1)
            oops.play()

        if self.rect.right > window.right:
            self.rect.center = window.center
            self.vector = self.set()
            computer.score.increase(1)
            oops.play()

        if pygame.sprite.spritecollide(self, paddles, False):
            pong.play()
            self.vector = -self.vector
            self.vector = self.vector * 1.1


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((SIZE*0.4, SIZE*3))
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


computer = Computer(window.left + 5, window.centery)
computer.add(all_sprites, paddles)

player = Player(window.right - 5, window.centery)
player.add(all_sprites, paddles)

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
