import sys
import os
import random
import pygame

# CONSTANTS
SCREEN_SIZE = (640, 480)
SCREEN_WIDTH = SCREEN_SIZE[0]
SCREEN_HEIGHT = SCREEN_SIZE[1]
BRICK_WIDTH = 64
BRICK_HEIGHT = 15
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARKGRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

# initialize stuff
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()


# paddle_hit = pygame.mixer.Sound('assets/pong_mid.wav')
# brick_hit = pygame.mixer.Sound('assets/pong_high.wav')
# floor_hit = pygame.mixer.Sound('assets/pong_low.wav')
# game_over_music = pygame.mixer.Sound('assets/game_over.flac')
# soundtrack = pygame.mixer.Sound('assets/soundtrack.wav')


class Paddle:
    ''' A virtual paddle.'''
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.delta_x = 8

    def update(self):
        keys = pygame.key.get_pressed()
        # detect key presses

        if keys[pygame.K_LEFT]:
            self.delta_x = -8
            self.rect.x += self.delta_x
        elif keys[pygame.K_RIGHT]:
            self.delta_x = 8
            self.rect.x += self.delta_x
        else:
            self.delta_x = 0

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Ball:
    ''' A virtual ball.'''
    def __init__(self, x, y, radius, game):
        self.game = game
        self.player = game.player
        self.radius = radius
        self.rect = pygame.Rect(x, y, radius*2, radius*2)
        self.pos = (self.rect.centerx, self.rect.centery)
        self.delta_x = random.choice(range(-5, 5))
        self.delta_y = 5
        self.hit_red = False
        self.modifier = 0

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y + self.modifier
        self.pos = (self.rect.centerx, self.rect.centery)

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.delta_x = -self.delta_x
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.delta_y = -self.delta_y

    def draw(self):
        pygame.draw.circle(screen, BLUE, self.pos, self.radius)

    def check_colisions(self):
        # ball hits paddle
        if self.rect.colliderect(self.player):
            # paddle_hit.play()

            if self.rect.left <= self.player.rect.left or self.rect.right >= self.player.rect.right:
                self.rect.bottom = self.player.rect.top

            self.delta_y = -self.delta_y
            if self.player.delta_x != 0:
                self.delta_x = self.player.delta_x // 2
            
            

        # ball hists bottom of window
        elif self.rect.bottom > SCREEN_HEIGHT:
            # floor_hit.play()
            self.game.lives -= 1
            if self.game.lives > 0:
                self.rect.centerx = self.player.rect.centerx
                self.rect.bottom = self.player.rect.top + 5
            else:
                self.game.game_over = True

        # ball hits a brick
        SCORES = {RED:4, ORANGE:3, GREEN:2, YELLOW:1}
        for brick in self.game.bricks:
            if self.rect.colliderect(brick):
                # brick_hit.play()

                if brick.color == RED and not self.hit_red:
                    self.delta_y *= 2
                    self.player.rect.width *= .5
                    self.hit_red = True
                self.game.score += SCORES[brick.color]
                self.delta_y = -self.delta_y
                self.game.bricks.remove(brick)
                break


class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Game:
    def __init__(self):
        self.player = Paddle(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT - 20, 100, 15)
        self.ball = Ball(SCREEN_WIDTH//2 - 5, SCREEN_HEIGHT//2 - 20, 10, self)
        self.lives = 3
        self.score = 0
        self.highscore = self.load_highscore()
        self.game_over = False
        self.bricks = []
        self.load_bricks()
        # soundtrack.play(-1)

    def load_highscore(self):
        try: 
            with open('highscore', 'r') as file:
                return int(file.read())
        except:
            return 0

    def save_highscore(self):
        try:
            with open('highscore', 'w') as file:
                file.write(str(self.score))
        except:
            pass

    def display_stats(self):
        status = "Score: %s  High Score: %s  Lives: %s" % (self.score, self.highscore, self.lives)
        font = pygame.font.Font(None, 28)
        text = font.render(status, True, WHITE)
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = 15
        screen.blit(text, textrect)

    def display_game_over(self):
        font = pygame.font.Font(None, 60)
        text = font.render("GAME OVER!!!!", True, RED)
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)
        # if not pygame.mixer.get_busy():
            # game_over_music.play()

    def load_bricks(self):
        COLORS = (RED, ORANGE, GREEN, YELLOW)
        index = 0
        y_offset = 40
        for row in range(8):
            x_offset = 0
            for column in range(SCREEN_WIDTH//BRICK_WIDTH):
                if column == 0 and row in (2, 4, 6):
                    index += 1
                self.bricks.append(
                    Brick(x_offset, y_offset, BRICK_WIDTH, BRICK_HEIGHT, COLORS[index]))
                x_offset += BRICK_WIDTH
            y_offset += BRICK_HEIGHT

    def draw_bricks(self):
        for brick in self.bricks:
            brick.draw()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type in (pygame.QUIT, pygame.KEYDOWN):
                    if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)
                        quit()
                    if event.key == pygame.K_n:
                        pygame.mixer.stop()
                        pygame.time.wait(1000)
                        Game().run()

            screen.fill(DARKGRAY)

            if not self.game_over:
                self.player.update()
                self.ball.update()
                self.ball.check_colisions()

                self.draw_bricks()
                self.player.draw()
                self.ball.draw()
            else:
                if self.score > self.highscore:
                    self.save_highscore()
                    self.highscore = self.load_highscore()
                soundtrack.stop()
                self.display_game_over()

            self.display_stats()

            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    Game().run()
