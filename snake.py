import pygame, random

pygame.init()
screen = pygame.display.set_mode((640, 480))
window = screen.get_rect()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

FPS = 15
BLOCKSIZE = 20
BLOCKWIDTH = int(window.width / BLOCKSIZE)
BLOCKHEIGHT = int(window.height / BLOCKSIZE)

def terminate():
    pygame.quit()
    quit()

class Block(pygame.sprite.Sprite):
    def __init__(self, fill, stroke, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, stroke, pygame.Rect(0, 0, self.rect.width, self.rect.height), 1)
        pygame.draw.rect(self.image, fill, pygame.Rect(1, 1, self.rect.width - 1, self.rect.height - 1))
        

class Worm(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.coords = [
            
        ]
        self.direction = 'right'


class Apple(Block):
    def __init__(self, fill, stroke, *groups):
        super().__init__(fill, stroke, *groups)
        self.set_location()

    def set_location(self):
        self.rect.x = random.randint(0, BLOCKWIDTH - 1)
        self.rect.y = random.randint(0, BLOCKHEIGHT - 1)

      
apple = Apple((255,0,0), (255,0,0), all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
