import math, random, pygame
pygame.init()

FPS = 10
WIDTH = 500
ROWS = 20
CELLSIZE = WIDTH // ROWS
BACKGROUND_COLOR = (50, 50, 50)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
GRID_COLOR = (128, 128, 128)

class Cube():
    def __init__(self, position, color=SNAKE_COLOR):
        self.position = position
        self.vector = pygame.Vector2(1, 0)
        self.color = color

    def draw(self, surface, eyes=False):
        size = WIDTH // ROWS
        i = self.position[0]
        j = self.position[1]
        pygame.draw.rect(surface, self.color, (i * size + 1, j * size + 1, size - 2, size - 2))
        if eyes:
            center = size // 2
            radius = 3
            left_eye = (i * size + center - radius, j * size + 8)
            right_eye = (i * size + size - radius * 2, j * size + 8)
            pygame.draw.circle(surface, (0, 0, 0), left_eye, radius)
            pygame.draw.circle(surface, (0, 0, 0), right_eye, radius)

    def move(self, dx, dy):
        self.vector = pygame.Vector2(dx, dy)
        self.position = (self.position[0] + self.vector.x, self.position[1] + self.vector.y)


class Snake():
    body = []
    turns = {}

    def __init__(self, position, color):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.vector = pygame.Vector2(0, 1)

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vector.x = -1
            self.vector.y = 0
            self.turns[self.head.position[:]] = [self.vector.x, self.vector.y]
        elif keys[pygame.K_RIGHT]:
            self.vector.x = 1
            self.vector.y = 0
            self.turns[self.head.position[:]] = [self.vector.x, self.vector.y]
        elif keys[pygame.K_UP]:
            self.vector.x = 0
            self.vector.y = -1
            self.turns[self.head.position[:]] = [self.vector.x, self.vector.y]
        elif keys[pygame.K_DOWN]:
            self.vector.x = 0
            self.vector.y = 1
            self.turns[self.head.position[:]] = [self.vector.x, self.vector.y]

        for index, cube in enumerate(self.body):
            position = cube.position[:]
            
            if position in self.turns:
                turn = self.turns[position]
                cube.move(turn[0], turn[1])
                if index == len(self.body) - 1:
                    self.turns.pop(position)
            else:
                if cube.vector.x == -1 and cube.position[0] <= 0:
                    cube.position = (ROWS - 1, cube.position[1])
                elif cube.vector.x == 1 and cube.position[0] >= ROWS - 1:
                    cube.position = (0, cube.position[1])
                elif cube.vector.y == 1 and cube.position[1] >= ROWS - 1:
                    cube.position = (cube.position[0], 0)
                elif cube.vector.y == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], ROWS - 1)
                else:
                    cube.move(cube.vector.x, cube.vector.y)
        
    def reset(self, position):
        self.head = Cube(position, color=SNAKE_COLOR)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.vector.x = 0
        self.vector.y = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.vector.x, tail.vector.y

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.position[0] - 1, tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.position[0] + 1, tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.position[0], tail.position[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.position[0], tail.position[1] + 1)))

        self.body[-1].vector.x = dx
        self.body[-1].vector.y = dy
        
def random_location(snake):

    snake_positions = snake.body
    while True:
        x = random.randrange(ROWS)
        y = random.randrange(ROWS)
        if len(list(filter(lambda z:z.position == (x, y), snake_positions))) > 0:
            # if this random location intersects with the snake, generate a new location
            continue
        else:
            break

    return (x, y)

def draw_grid(surface):
    x = y = 0
    for line in range(ROWS):
        x = x + CELLSIZE
        y = y + CELLSIZE

        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, WIDTH))
        pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y))

def game_over():
    pygame.quit()
    quit()

def main():
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("SNAKE!")
    window = screen.get_rect()
    clock = pygame.time.Clock()

    snake = Snake((10, 10), color=SNAKE_COLOR)
    apple = Cube(random_location(snake), color=APPLE_COLOR)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over()

        snake.move()
        if snake.body[0].position == apple.position:
            snake.add_cube()
            apple = Cube(random_location(snake), color=APPLE_COLOR)

        screen.fill(BACKGROUND_COLOR)
        snake.draw(screen)
        apple.draw(screen)
        draw_grid(screen)
        pygame.display.update()
        clock.tick(FPS)
        # pygame.time.delay(50)

main()