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
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def draw_board(screen, selected_piece, valid_moves):
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if (row + col) % 2 == 0 else RED
            pygame.draw.rect(screen, color, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Highlight the selected piece and valid moves only if a piece is selected
    if selected_piece:
        sx, sy = selected_piece
        pygame.draw.rect(screen, YELLOW, (sx * SQUARE_SIZE, sy * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  # Highlight selected piece

        # Highlight valid moves
        for move in valid_moves:
            _, (end_x, end_y) = move
            pygame.draw.rect(screen, BLUE, (end_x * SQUARE_SIZE, end_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)  # Draw a blue border


def draw_pieces(screen, board):
    for x in range(ROWS):
        for y in range(COLS):
            piece = board[y][x]
            if piece != '.':
                color = WHITE if piece.lower() == 'w' else GREY
                pygame.draw.circle(screen, color, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = x // SQUARE_SIZE
    col = y // SQUARE_SIZE
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
                    print(f"Starting pos: {selected_piece}")
                    start, end = selected_piece, (row, col)
                    if end in [move[1] for move in valid_moves]:
                        print(f"Ending move: {end}")
                        game.make_move(start, end)
                        print(f"Moved from {start} to {end}")
                        selected_piece = None
                        valid_moves = []
                    else:
                        print("Invalid move. Try again.")
                        selected_piece = None  # Optionally deselect on invalid move
                else:
                    selected_piece = (row, col)
                    print(f"Selected piece at row {row}, col {col}")
                    valid_moves = game.valid_moves((row, col))  # Ensure this fetches correct piece
                    print(f"Valid moves from ({row}, {col}): {valid_moves}")

        draw_board(screen, selected_piece, valid_moves)
        draw_pieces(screen, game.board)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
