import pygame
import sys
from pvp_checkers_helper import Checkers

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
crown_image = pygame.image.load('../images/crown.png')
crown_image = pygame.transform.scale(crown_image, (SQUARE_SIZE//2, SQUARE_SIZE//2))

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
                center_x = x * SQUARE_SIZE + SQUARE_SIZE // 2
                center_y = y * SQUARE_SIZE + SQUARE_SIZE // 2

                if piece.lower() == 'w': 
                    color = WHITE
                elif piece.lower() == 'b':
                    color = GREY 
                pygame.draw.circle(screen, color, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)

                # Draw crown if the piece is a king
                if piece.isupper():
                    screen.blit(crown_image, (center_x - crown_image.get_width() // 2, center_y - crown_image.get_height() // 2))

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
    current_player = 'w'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(f"Selected piece: {(row, col)}")
                if selected_piece and (row, col) in [move[1] for move in valid_moves]:
                    further_moves = game.make_move(selected_piece, (row, col))
                    print(f"Moved from {selected_piece} to {(row, col)}")
                    if not further_moves:
                        selected_piece = None
                        valid_moves = []
                        current_player = 'b' if current_player == 'w' else 'w'
                    else:
                        selected_piece = (row, col)
                        valid_moves = further_moves
                elif game.board[col][row] != '.' and game.board[col][row].lower() == current_player:
                    selected_piece = (row, col)
                    valid_moves = game.valid_moves((row, col))

        draw_board(screen, selected_piece, valid_moves)
        draw_pieces(screen, game.board)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
