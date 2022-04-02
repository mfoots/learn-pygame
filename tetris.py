import pygame, random
pygame.init()

FPS = 60
BLOCK_SIZE = 40
GRID_SIZE = (BLOCK_SIZE*10, BLOCK_SIZE*20)
GAME_SIZE = (GRID_SIZE[0] + 300, GRID_SIZE[1] + 1)
BACKGROUND = (25, 25, 25)
GRID_COLOR = (100, 100, 100)

COLORS = [
    (0, 255, 255),    # I - Cyan
    (255, 50, 19),    # Z - Red
    (114, 203, 59),   # S - Green
    (3, 65, 174),     # J - Blue
    (255, 151, 28),   # L - Orange
    (0, 255, 255),    # T - Purple
    (255, 213, 0),    # O - Yellow
]

'''
GRID
0   1   2   3 
4   5   6   7
8   9   10  11
12  13  14  15

# Tetrominoes
# SHAPES = (
#     ((1, 5, 9, 13), (4, 5, 6, 7)),  # I-block
#     ((4, 5, 9, 10), (2, 6, 5, 9)),  # Z-block
#     ((6, 7, 9, 10), (1, 5, 6, 10)), # S-block
#     ((1, 2, 5, 9), (0, 4, 5, 6), (1, 5, 9, 8), (4, 5, 6, 10)),   # J-block
#     ((1, 2, 6, 10), (5, 6, 7, 9), (2, 6, 10, 11), (3, 5, 6, 7)), # L-block
#     ((1, 4, 5, 6), (1, 4, 5, 9), (4, 5, 6, 9), (1, 5, 6, 9)),    # T-block
#     ((1, 2, 4, 6)), # O-block
# )
'''

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

    def convert_shape(self):
        potitions = []
        orientation = self.shape[self.rotation % len(self.shape)]
        

block = Block(5, 0, random.choice(SHAPES))

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
