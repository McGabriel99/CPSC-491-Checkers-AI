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
BLUE = (0,0,255)

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

# Convert mouse position to board coordinates
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



def highlight_moves(screen, valid_moves):
    for _, (row, col) in valid_moves:  # Ensure we only highlight the destination squares
        pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)



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
                if selected_piece and (row, col) in [mv[1] for mv in valid_moves]:
                    # Attempt to make a move only if the click is on a valid move position
                    move_result = game.make_move(selected_piece, (row, col), valid_moves)
                    if move_result:
                        selected_piece = None
                        valid_moves = []
                        game.switch_player()  # Switch turns only on a successful move
                    else:
                        selected_piece = None  # Deselect on failed move
                        valid_moves = []
                elif game.board[row][col].lower() == game.current_player and game.board[row][col] != '.':
                    selected_piece = (row, col)
                    valid_moves = game.get_valid_moves(selected_piece)
                    print(valid_moves)  # Debug print moved here to show only when a piece is selected

        draw_board(screen)
        draw_pieces(screen, game.board)
        highlight_moves(screen, [mv[1] for mv in valid_moves])
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()
