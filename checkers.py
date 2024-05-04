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

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_king(self, piece):
        # Assuming kings are uppercase
        return piece.isupper()

    def valid_moves(self, piece_position):
        x, y = piece_position
        moves = []
        player = self.board[y][x].lower()
        directions = [(-1, -1), (-1, 1)] if player == 'w' else [(1, -1), (1, 1)]

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # Normal move
            if 0 <= ny < 8 and 0 <= nx < 8 and self.board[ny][nx] == '.':
                moves.append(((x, y), (nx, ny)))
            # Capture move
            elif 0 <= ny < 8 and 0 <= nx < 8 and self.board[ny][nx].lower() != player and self.board[ny][nx] != '.':
                ny2, nx2 = ny + dy, nx + dx
                if 0 <= ny2 < 8 and 0 <= nx2 < 8 and self.board[ny2][nx2] == '.':
                    moves.append(((x, y), (nx2, ny2)))

        return moves



    def make_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        self.board[y2][x2] = self.board[y1][x1]  # Move the piece
        self.board[y1][x1] = '.'  # Clear the original position

    def ai_move(self, player):
        moves = self.valid_moves(player)
        # This is a simple AI: Just pick the first available move
        return moves[0] if moves else None

def main():
    game = Checkers()
    current_player = 'w'  # Start with white

    while True:
        game.print_board()
        if current_player == 'w':
            print("Your turn (White).")
            moves = game.valid_moves('w')
            if not moves:
                print("No moves available. Game over.")
                break
            print("Available moves:", moves)
            move = input("Enter your move (e.g., '1,2 to 3,4'): ")
            move = move.split(" to ")
            start = tuple(map(int, move[0].split(',')))
            end = tuple(map(int, move[1].split(',')))
            if (start, end) in moves:
                game.make_move((start, end))
                current_player = 'b'
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn (Black).")
            move = game.ai_move('b')
            if not move:
                print("No moves available. Game over.")
                break
            print("AI moves from", move[0], "to", move[1])
            game.make_move(move)
            current_player = 'w'

if __name__ == "__main__":
    main()
