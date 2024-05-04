import pygame
import sys
from checkers import Checkers

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def draw_board(screen):
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    for y in range(ROWS):
        for x in range(COLS):
            piece = board[y][x]
            if piece != '.':
                color = WHITE if piece.lower() == 'w' else GREY
                pygame.draw.circle(screen, color, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    print(f"Selected row: {row}, col: {col}")
    return row, col

def main():
    clock = pygame.time.Clock()
    game = Checkers()
    running = True
    selected_piece = None
    valid_moves = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if selected_piece:
                    start, end = selected_piece, (row, col)
                    if end in [move[1] for move in valid_moves]:  # Check if end position is in valid_moves
                        game.make_move(start, end)
                        selected_piece = None
                        valid_moves = []
                    else:
                        print("Invalid move. Try again.")
                        selected_piece = None  # Deselect piece on invalid move
                else:
                    selected_piece = (row, col)
                    valid_moves = game.valid_moves(game.board[row][col])  # Ensure this fetches correct piece


        draw_board(screen)
        draw_pieces(screen, game.board)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
