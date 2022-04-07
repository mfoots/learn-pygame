import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Apple Catch Game")
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

apple_img = pygame.image.load('assets/apple.png').convert_alpha()
bowl_img = pygame.image.load('assets/bowl.png').convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = bowl_img
        self.rect = self.image.get_rect(midbottom = (window.centerx, window.height - 60))
        self.score = Scoreboard(all_sprites)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > window.width:
            self.rect.right = window.width


class Apple(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = apple_img
        self.rect = self.image.get_rect(midbottom = (window.centerx, -60))
        self.vector = pygame.Vector2(0, 2)

    def reset_apple(self):
        self.rect.top = -60
        self.rect.left = random.randint(60, window.width - 60)
        self.vector.y = random.randint(2,5)
        

    def update(self):
        self.rect.move_ip(self.vector)
        
        if self.rect.bottom > window.height - 60:
            self.reset_apple()
            player.score.change(-1)

        if pygame.sprite.collide_rect(self, player):
            self.reset_apple()
            player.score.change()


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
        self.image = self.font.render(f"Apples caught: {self.score}", True, (255, 255, 255))
        self.rect = self.image.get_rect(midleft=(20, window.height - 30))

apple = Apple(all_sprites)
player = Player(all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    all_sprites.update()
    screen.fill((87, 238, 255))
    pygame.draw.rect(screen, (49, 173, 0), pygame.Rect(0, 400, 640, 80))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)