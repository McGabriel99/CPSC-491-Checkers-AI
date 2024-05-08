class Checkers:
    def __init__(self):
        # Initialize the board with 'b' for black, 'w' for white, and '.' for empty
        self.board = [
            ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
            ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
            ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 'w', '.', 'w', '.', 'w', '.', 'w'],
            ['w', '.', 'w', '.', 'w', '.', 'w', '.'],
            ['.', 'w', '.', 'w', '.', 'w', '.', 'w']
        ]

    def is_king(self, piece):
        return piece.isupper()

    def valid_moves(self, piece_position):
        x, y = piece_position
        moves = []
        piece = self.board[y][x]
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] if self.is_king(piece) else ([(-1, -1), (-1, 1)] if piece.lower() == 'w' else [(1, -1), (1, 1)])

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # Normal move
            if 0 <= ny < 8 and 0 <= nx < 8 and self.board[ny][nx] == '.':
                moves.append(((x, y), (nx, ny)))
            # Capture move
            elif 0 <= ny < 8 and 0 <= nx < 8 and self.board[ny][nx].lower() != piece and self.board[ny][nx] != '.':
                ny2, nx2 = ny + dy, nx + dx
                if 0 <= ny2 < 8 and 0 <= nx2 < 8 and self.board[ny2][nx2] == '.':
                    moves.append(((x, y), (nx2, ny2)))

        return moves



    def make_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        self.board[y2][x2] = self.board[y1][x1]  # Move the piece
        self.board[y1][x1] = '.'  # Clear the original position

        # Check if the move is a jump
        if abs(x2 - x1) == 2 or abs(y2 - y1) == 2:
            jumped_x = x1 + (x2 - x1) // 2
            jumped_y = y1 + (y2 - y1) // 2
            self.board[jumped_y][jumped_x] = '.'  # Remove the jumped piece

        # check for promotion to king
        if (y2 == 0 and self.board[y2][x2] == 'w') or (y2 == 7 and self.board[y2][x2] == 'b'):
            self.board[y2][x2] = self.board[y2][x2].upper()
            print(f"Promoted to king: {self.board[y2][x2]}")

    # def ai_move(self, player):
    #     moves = self.valid_moves(player)
    #     # This is a simple AI: Just pick the first available move
    #     return moves[0] if moves else None