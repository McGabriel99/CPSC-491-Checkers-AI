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
        self.current_player = 'w'

    def switch_player(self):
        self.current_player = 'b' if self.current_player == 'w' else 'w'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def get_valid_moves(self, pos):
        x, y = pos
        piece = self.board[y][x]
        print(f"Checking moves for {piece} at ({x}, {y})")
        if piece.lower() != self.current_player or piece == '.':
            return []
        moves = []
        player = piece.lower()
        directions = [(-1, -1), (-1, 1)] if player == 'w' or piece.isupper() else [(1, -1), (1, 1)]
        if piece.isupper():
            directions.extend([(-d[0], -d[1]) for d in directions])
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and self.board[ny][nx] == '.':
                moves.append(((x, y), (nx, ny)))
            elif 0 <= nx < 8 and 0 <= ny < 8 and self.board[ny][nx].lower() != player and self.board[ny][nx] != '.':
                jx, jy = nx + dx, ny + dy
                if 0 <= jx < 8 and 0 <= jy < 8 and self.board[jy][jx] == '.':
                    moves.append(((x, y), (jx, jy)))
        return moves
    
    def get_directions(self, piece):
        if piece == 'w':
            return [(-1, -1), (-1, 1)]  # Normal white moves up
        elif piece == 'b':
            return [(1, -1), (1, 1)]  # Normal black moves down
        else:
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Kings move in all directions



    def make_move(self, start, end, valid_moves):
        if (start, end) in valid_moves:
            x1, y1 = start
            x2, y2 = end
            self.board[y2][x2] = self.board[y1][x1]
            self.board[y1][x1] = '.'
            # Remove the jumped piece if it's a capture move
            if abs(x2 - x1) == 2 or abs(y2 - y1) == 2:
                mx, my = (x1 + x2) // 2, (y1 + y2) // 2
                self.board[my][mx] = '.'
            return True
        return False


    def ai_move(self, player):
        moves = self.get_valid_moves(player)
        # This is a simple AI: Just pick the first available move
        return moves[0] if moves else None

def main():
    game = Checkers()
    current_player = 'w'  # Start with white

    while True:
        game.print_board()
        if current_player == 'w':
            print("Your turn (White).")
            moves = game.get_valid_moves('w')
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
