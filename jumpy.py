# Michael Foots
import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((550, 600))
pygame.display.set_caption("Jumpy")
win = screen.get_rect()
clock = pygame.time.Clock()
allsprites = pygame.sprite.RenderPlain()
platforms = pygame.sprite.RenderPlain()


class Player(pygame.sprite.Sprite):
    def __init__(self, platforms):
        super().__init__()
        self.platforms = platforms
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color(230, 70, 0))
        # self.rect = self.image.get_rect(midbottom=(win.centerx, win.height))
        self.rect = self.image.get_rect(midbottom=(50, win.height - 150))
        self.is_jumping = False
        self.dy = 0
        
    def move(self, dx):
        self.rect.centerx += dx

    def jump(self):
        if not self.is_jumping:
            self.dy = -10
            self.is_jumping = True

    def fall(self):
        if self.dy == 0:
            self.dy = 1.5
        else:
            self.dy += .38
        self.rect.bottom += self.dy

    def update(self):
        if self.is_jumping:
            self.fall()
            platform_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
            for platform in platform_hit_list:
                if self.dy > 0:
                    self.rect.bottom = platform.rect.top
                    self.is_jumping = False
                    self.dy = 0
                elif self.dy < 0:
                    self.rect.top = platform.rect.bottom
                    self.rect.y += 2
                    self.fall()
                
            if self.rect.bottom >= win.height:
                self.rect.bottom = win.height
                self.is_jumping = False
                self.dy = 0
        else:
            self.rect.bottom += 2
            check = pygame.sprite.spritecollide(self, self.platforms, False)
            self.rect.bottom -= 2
            if len(check) == 0:
                self.fall()
                self.is_jumping = True

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 25))
        self.image.fill(pygame.Color(0, 85, 232))
        self.rect = self.image.get_rect(center = (x, y))

platform_locations = [
    (200, win.height-100),
    (275, win.height - 200),
    (150, win.height - 300)
]
for location in platform_locations:
    platform = Platform(*location)
    platform.add(platforms, allsprites)

player = Player(platforms)
player.add(allsprites)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
                quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.jump()
    if keys[pygame.K_LEFT]:
        player.move(-5)
    if keys[pygame.K_RIGHT]:
        player.move(5)

    allsprites.update()
    screen.fill(pygame.Color(170, 250, 255))
    allsprites.draw(screen)
    pygame.display.flip()
