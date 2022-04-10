import pygame, random
pygame.init()

#Global Variables
# FPS = 60
BACKGROUND_COLOR = (50, 50, 50)
TEXT_COLOR = (255, 255, 255)
LINE_COLOR = (128, 128, 128)
BORDER_COLOR = (255, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAY_WIDTH = 250
PLAY_HEIGHT = 500
BLOCK_SIZE = 25
COLUMN_COUNT = 10
ROW_COUNT = 20

TOP_LEFT_X = (SCREEN_WIDTH - PLAY_WIDTH) // 2
TOP_LEFT_Y = SCREEN_HEIGHT - PLAY_HEIGHT - 10

# Tetrominoes

S = [[
        '.....',
        '.....',
        '..00.',
        '.00..',
        '.....'],
    [
        '.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

Z = [[
        '.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
    [
        '.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']]

I = [[
        '..0..',
        '..0..',
        '..0..',
        '..0..',
        '.....'],
    [
        '.....',
        '0000.',
        '.....',
        '.....',
        '.....']]

O = [
        '.....',
        '.....',
        '.00..',
        '.00..',
        '.....']

J = [[
        '.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
    [
        '.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
    [
        '.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
    [
        '.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

L = [
    [
        '.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
    [
        '.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
    [
        '.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
    [
        '.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']]

T = [[
        '.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
    [
        '.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
    [
        '.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
    [
        '.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]

SHAPE_LIST = [S, Z, I, O, J, L, T]
SHAPE_COLORS = [
    (0, 255, 255),    # I - Cyan
    (255, 50, 19),    # Z - Red
    (114, 203, 59),   # S - Green
    (3, 65, 174),     # J - Blue
    (255, 151, 28),   # L - Orange
    (0, 255, 255),    # T - Purple
    (255, 213, 0)     # O - Yellow
]

class Piece():
    def __init__(self, column, row, shape):
        '''Representas a falling tetris piece with attributes
        col, row, shape, color, rotation, and tile_pos'''
        self.col = column
        self.row = row
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPE_LIST.index(shape)]
        self.rotation = 0
        self.tile_pos = None
    
    def get_piece_tile_pos(self):
        '''Return a positions list representing the row and column
        index of each falling tile'''
        positions = []
        shape_list = self.shape[self.rotation % len(self.shape)]

        # get tile positions
        for row_index, line in enumerate(shape_list):
            row = list(line)
            for col_index, column in enumerate(row):
                if column == '0':
                    positions.append((self.row + row_index, self.col + col_index))

        # offset positions
        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 4, pos[1] - 2)

        self.tile_pos = positions
        return self.tile_pos
    
    def is_valid_pos(self):
        '''Check if falling tetris peice conflicts with existing tiles'''
        self.get_piece_tile_pos()
        # list comprehension
        accepted_positions = [[(i, j) for j in range(10) if grid[i][j] == BACKGROUND_COLOR] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]

        for pos in self.get_piece_tile_pos():
            if pos not in accepted_positions:
                if pos[0] > -1:
                    return False

        return True

    def draw_current_piece(self, surface):
        '''Draw each tile according to the tile positions'''
        if self.tile_pos is not None:
            for pos in self.tile_pos:
                pygame.draw.rect(surface, self.color, (TOP_LEFT_X + pos[1] * BLOCK_SIZE, \
                    TOP_LEFT_Y + pos[0] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)


    def draw_next_piece(self, surface):
        '''Draw the next peice to the right of the playing window'''
        font = pygame.font.SysFont(None, 30)
        label = font.render("Next Shape", 1, (TEXT_COLOR))
        shape_list = self.shape[self.rotation % len(self.shape)]

        surface_x = TOP_LEFT_X + PLAY_WIDTH + 50
        surface_y = TOP_LEFT_Y + PLAY_HEIGHT/2 - 100

        for row_index, line in enumerate(shape_list):
            row = list(line)
            for col_index, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, self.color, (surface_x + col_index * BLOCK_SIZE, \
                    surface_y + row_index * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        surface.blit(label, (surface_x + 10, surface_y - 30))

def check_lost():
    '''Check to see if any position on the first row of grid is occupied.
    If so, then the game is over.'''
    for i in range(COLUMN_COUNT):
        if grid[0][i] != BACKGROUND_COLOR:
            return True
    return False 

def draw_text_middle(text, size, color, surface):
    '''Draw the starting text and show it in the middle of the window.'''
    font = pygame.font.SysFont(None, size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH/2 - (label.get_width()/2), \
        TOP_LEFT_Y + PLAY_HEIGHT/2 - label.get_height()/2))

def draw_score(surface):
    global score
    font = pygame.font.SysFont(None, 30)
    label = font.render(f'Score: {score}', 1, (TEXT_COLOR))
    surface_x = TOP_LEFT_X - label.get_width() - 100
    surface_y = TOP_LEFT_Y + PLAY_HEIGHT/2 - 100
    surface.blit(label, (surface_x + 10, surface_y - 30))

def draw_grid(surface, row, col):
    surface_x = TOP_LEFT_X
    surface_y = TOP_LEFT_Y
    # draw the horizontal lines
    for i in range(row):
        pygame.draw.line(surface, LINE_COLOR, (surface_x, surface_y + i * BLOCK_SIZE), \
            (surface_x + PLAY_WIDTH, surface_y + i * BLOCK_SIZE))
    # draw the vertical lines
    for j in range(col):
        pygame.draw.line(surface, LINE_COLOR, (surface_x + j * BLOCK_SIZE, surface_y), \
            (surface_x + j * BLOCK_SIZE, surface_y + PLAY_HEIGHT))

def clear_rows():
    global score

    inc = 0
    row_index = ROW_COUNT - 1
    while row_index > -1:
        # start from the bottom and check it any row could be cleared
        clear = True
        for col_index in range(COLUMN_COUNT):
            if grid[row_index][col_index] == BACKGROUND_COLOR:
                clear = False
                break

        if clear:
            # if one row could be cleared, delete this row's info
            # from grid then insert an empty row at the position
            inc += 1
            del grid[row_index]
            grid.insert(0, [])
            for i in range(COLUMN_COUNT):
                grid[0].insert(i, BACKGROUND_COLOR)
        else:
            row_index -= 1

        if row_index == inc:
            # if clearing two or more, score increases more
            score += (inc**2) * 10
            break

def draw_existing_tiles(surface):
    surface.fill(BACKGROUND_COLOR)
    # Tetris Tile
    font = pygame.font.SysFont(None, 60)
    label = font.render('Tetris', 1, TEXT_COLOR)

    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH/2 - (label.get_width()/2), 30))

    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] != BACKGROUND_COLOR:
                pygame.draw.rect(surface, grid[row_index][col_index], \
                    (TOP_LEFT_X + col_index * BLOCK_SIZE, TOP_LEFT_Y + row_index * BLOCK_SIZE, \
                        BLOCK_SIZE, BLOCK_SIZE), 0)

def main():
    global grid
    global score

    # 20 row, 10 column grid
    grid = [[BACKGROUND_COLOR for x in range(10)] for x in range(20)]

    score = 0
    block_accelerate = False
    change_piece = False
    run = True
    current_piece = Piece(5, 0, random.choice(SHAPE_LIST))
    next_piece = Piece(5, 0, random.choice(SHAPE_LIST))
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        fall_speed = 0.27
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 >= fall_speed or block_accelerate:
            # the falling piece decides how fast to fall
            fall_time = 0
            current_piece.row += 1
            block_accelerate = False
            if not (current_piece.is_valid_pos()) and current_piece.row > -1:
                # if the falling piece falls to an invalide position, go back
                # one row and then "change piece" 
                current_piece.row -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.display.quit()
                    quit()

                if event.key == pygame.K_LEFT:
                    current_piece.col -= 1
                    if not current_piece.is_valid_pos():
                        current_piece.col += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.col += 1
                    if not current_piece.is_valid_pos():
                        current_piece.col -= 1
                
                elif event.key == pygame.K_UP:
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not current_piece.is_valid_pos():
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)


                if event.key == pygame.K_DOWN or event.key == pygame.K_SPACE:
                    block_accelerate = True
                    current_piece.row += 1
                    if not current_piece.is_valid_pos():
                        current_piece.row -= 1

        current_piece.get_piece_tile_pos()
        draw_existing_tiles(screen)
        current_piece.draw_current_piece(screen)

        if change_piece:
            for item in current_piece.tile_pos:
                row, column = item
                if row > -1:
                    grid[row][column] = current_piece.color

            current_piece = next_piece
            next_piece = Piece(5, 0, random.choice(SHAPE_LIST))
            change_piece = False
            clear_rows()
        
        next_piece.draw_next_piece(screen)

        draw_grid(screen, 20, 10)
        pygame.draw.rect(screen, BORDER_COLOR, (TOP_LEFT_X, TOP_LEFT_Y, \
            PLAY_WIDTH, PLAY_HEIGHT), 5)
        draw_score(screen)
        pygame.display.update()

        if check_lost():
            run = False

    draw_text_middle("YOU LOOSE!", 40, TEXT_COLOR, screen)
    pygame.display.update()
    pygame.time.delay(2000)
    
def main_menu():
    run = True
    while run:
        screen.fill(BACKGROUND_COLOR)
        draw_text_middle("Press any key to begin.", 60, TEXT_COLOR, screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()




screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')
window = screen.get_rect()

main_menu()