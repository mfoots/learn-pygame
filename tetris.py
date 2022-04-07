import pygame, random
pygame.init()

FPS = 30
BLOCK_SIZE = 40
GRID_SIZE = (BLOCK_SIZE*10, BLOCK_SIZE*20)
GAME_SIZE = (GRID_SIZE[0] + 300, GRID_SIZE[1] + 1)
BACKGROUND = (25, 25, 25)
GRID_COLOR = (100, 100, 100)
BLANK = '.'

COLORS = [
    (0, 255, 255),    # I - Cyan
    (255, 50, 19),    # Z - Red
    (114, 203, 59),   # S - Green
    (3, 65, 174),     # J - Blue
    (255, 151, 28),   # L - Orange
    (0, 255, 255),    # T - Purple
    (255, 213, 0),    # O - Yellow
]

# Tetrominoes

S = [
    [
        '.....',
        '.....',
        '..00.',
        '.00..',
        '.....',
    ],
    [
        '.....',
        '..0..',
        '..00.',
        '...0.',
        '.....',
    ],
]

Z = [
    [
        '.....',
        '.....',
        '.00..',
        '..00.',
        '.....',
    ],
    [
        '.....',
        '..0..',
        '.00..',
        '.0...',
        '.....',
    ],
]

I = [
    [
        '..0..',
        '..0..',
        '..0..',
        '..0..',
        '.....',
    ],
    [
        '.....',
        '0000.',
        '.....',
        '.....',
        '.....',
    ],
]

O = [
        '.....',
        '.....',
        '.00..',
        '.00..',
        '.....',
    ]

J = [
    [
        '.....',
        '.0...',
        '.000.',
        '.....',
        '.....',
    ],
    [
        '.....',
        '..00.',
        '..0..',
        '..0..',
        '.....',
    ],
    [
        '.....',
        '.....',
        '.000.',
        '...0.',
        '.....',
    ],
    [
        '.....',
        '..0..',
        '..0..',
        '.00..',
        '.....',
    ],
]

L = [
    [
        '.....',
        '...0.',
        '.000.',
        '.....',
        '.....',
    ],
    [
        '.....',
        '..0..',
        '..0..',
        '..00.',
        '.....',
    ],
    [
        '.....',
        '.....',
        '.000.',
        '.0...',
        '.....',
    ],
    [
        '.....',
        '.00..',
        '..0..',
        '..0..',
        '.....',
    ],
]

T = [
    [
        '.....',
        '..0..',
        '.000.',
        '.....',
        '.....',
    ],
    [
        '.....',
        '..0..',
        '..00.',
        '..0..',
        '.....',
    ],
    [
        '.....',
        '.....',
        '.000.',
        '..0..',
        '.....',
    ],
    [
        '.....',
        '..0..',
        '.00..',
        '..0..',
        '.....',
    ]
]

SHAPES = [S, Z, I, O, J, L, T]

class Block:
    x = y = n = 0

    def __init__(self, row, column, shape):
        self.row = row
        self.column = column
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.rotation = 0


block = Block(1, 1, random.choice(SHAPES))

screen = pygame.display.set_mode(GAME_SIZE, pygame.NOFRAME)
window = screen.get_rect()
clock = pygame.time.Clock()

def close_window():
    pygame.quit()
    quit()

def draw_grid():
    # vertical lines
    for i in range(11):
        x = BLOCK_SIZE * i
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, GRID_SIZE[1]))

    # horizontal lines
    for i in range(21):
        y = BLOCK_SIZE * i
        pygame.draw.line(screen, GRID_COLOR, (0, y), (GRID_SIZE[0], y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close_window()

    screen.fill(BACKGROUND)
    draw_grid()
    pygame.display.update()
    clock.tick(FPS)
