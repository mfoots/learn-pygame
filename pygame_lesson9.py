import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
window = screen.get_rect()
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

class Ship(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.original_image = pygame.Surface((25,25))
        self.original_image.fill((0,0,0))
        self.original_image.set_colorkey((0,0,0))
        
        self.image = self.original_image
        self.rect = self.image.get_rect()
        points = [
            self.rect.bottomleft,
            self.rect.midtop,
            self.rect.bottomright,
            (self.rect.centerx, self.rect.centery + 5)
        ]
        pygame.draw.polygon(self.image, (255,255,255), points, 1)
        self.rect.center = window.center

        self.speed = 0
        self.angle = 0
        self.vector = pygame.Vector2(0,0)
        self.pivot = pygame.Vector2(self.rect.center)
        self.offset = pygame.Vector2(0,0)
        
    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pivot + self.offset.rotate(self.angle))
        self.angle %= 360

    def check_key_events(self):
        keys = pygame.key.get_pressed()
        # turn left or right
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        # thrust
        if keys[pygame.K_UP]:
            self.speed += 0.5

    def loop(self):
        # loop from left to right side
        if self.rect.right < 0:
            self.rect.move_ip(window.width, 0)
            self.vector.x += window.width
        # loop from right to left side
        if self.rect.left > window.width:
            self.rect.move_ip(-window.width, 0)
            self.vector.x -= window.width
        # loop from top to bottom
        if self.rect.bottom < 0:
            self.rect.move_ip(0, window.height)
            self.vector.y += window.height
        # loop from bottom to top
        if self.rect.top > window.height:
            self.rect.move_ip(0, -window.height)
            self.vector.y -= window.height

        
    def thrust(self):
        self.vector.x += self.speed * math.sin(math.radians(self.angle)) * -1
        self.vector.y += self.speed * math.cos(math.radians(self.angle)) * -1
        self.rect.move_ip(self.vector)
        self.speed *= .98 # friction in space?
        

    def update(self):
        self.check_key_events()
        self.rotate()
        self.thrust()
        self.loop()


ship = Ship(all_sprites)

def stars(size):
    star_surface = pygame.Surface((size, size))
    star_rect = star_surface.get_rect()
    pygame.draw.circle(star_surface, (255,255,255), (0, 0), size * 0.5)
    star_rect.center = (random.randint(0, window.width),
                        random.randint(0, window.height))
    screen.blit(star_surface, star_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    all_sprites.update()
    screen.fill((0, 0, 0))
    stars(10)
    pygame.draw.rect(screen, (100,100,100), window, 3)
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)
