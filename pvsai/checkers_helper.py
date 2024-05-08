import random

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
        is_piece_king = self.is_king(piece)
        print(f"Checking moves for {'King' if is_piece_king else 'Man'} at ({x}, {y})")
        own_color = piece.lower()
        opponent_color = 'b' if own_color == 'w' else 'w'

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] if is_piece_king else ([(-1, -1), (-1, 1)] if piece.lower() == 'w' else [(1, -1), (1, 1)])
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                if self.board[ny][nx] == '.':
                    moves.append(((x, y), (nx, ny)))
                elif self.board[ny][nx].lower() == opponent_color:
                    ny2, nx2 = ny + dy, nx + dx
                    if 0 <= ny2 < 8 and 0 <= nx2 < 8 and self.board[ny2][nx2] == '.':
                        moves.append(((x, y), (nx2, ny2)))

        for move in moves:
            print(f"Generated move from ({x}, {y}) to {move[1]}")
        return moves
    
    def additional_captures(self, position):
        # Check if there are additional captures from the new position
        return [move for move in self.valid_moves(position) if abs(move[1][0] - position[0]) == 2]


    def make_move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        self.board[y2][x2] = self.board[y1][x1]  # Move the piece
        self.board[y1][x1] = '.'  # Clear the original position
        capture_occurred = False

        if abs(x2 - x1) == 2 or abs(y2 - y1) == 2:
            jumped_x = (x1 + x2) // 2
            jumped_y = (y1 + y2) // 2
            self.board[jumped_y][jumped_x] = '.'
            capture_occurred = True
        
        #check for promotion to king
        promotion_occurred = False
        if (y2 == 0 and self.board[y2][x2] == 'w') or (y2 == 7 and self.board[y2][x2] == 'b'):
            self.board[y2][x2] = self.board[y2][x2].upper()
            print(f"Promoted to king: {self.board[y2][x2]}")
            promotion_occurred = True

        if capture_occurred:
            further_captures = self.additional_captures((x2, y2))
            if further_captures:
                return further_captures
            elif promotion_occurred:
                # If promoted but no further captures, prevent additional moves
                return None
        return None
    
    def evaluate_board(self):
        score = 0
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece:
                    piece_value = 25 if piece.isupper() else 5
                    piece_score = piece_value if piece.lower() == 'b' else -piece_value
                    score += piece_score
                    print(f"Piece {piece} at ({x}, {y}) contributes {piece_score} to score")
        print(f"Total board evaluation score: {score}")
        return score
    
    def minimax(self, board, depth, maximizing_player, game, alpha, beta):
        if depth == 0 or self.is_game_over():
            return self.evaluate_board(), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_all_moves('b'):
                simulation_board = self.simulate_move(move)
                eval = self.minimax(simulation_board, depth - 1, False, game, alpha, beta)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            print(f"At depth {depth}, best move is {best_move} with eval {max_eval if maximizing_player else min_eval}")
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_all_moves('w'):
                simulation_board = self.simulate_move(move)
                eval = self.minimax(simulation_board, depth - 1, True, game, alpha, beta)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
        
    def simulate_move(self, move):
        """ Simulate a move to evaluate potential board states for Minimax. """
        # Extract start and end positions from the move
        start, end = move
        x1, y1 = start
        x2, y2 = end

        # Create a deep copy of the board to simulate the move without altering the actual game state
        new_board = [row[:] for row in self.board]
        
        # Perform the move on the new board
        new_board[y2][x2] = new_board[y1][x1]
        new_board[y1][x1] = '.'

        # Handle captures
        if abs(x2 - x1) == 2 or abs(y2 - y1) == 2:
            jumped_x = (x1 + x2) // 2
            jumped_y = (y1 + y2) // 2
            new_board[jumped_y][jumped_x] = '.'

        # Return the new simulated board state
        return new_board
    
    def undo_move(self, move):
        """ Undo a move (might not be needed if always simulating on copied boards). """
        pass

    def is_game_over(self):
        """ Check if the game is over based on remaining pieces and possible moves. """
        has_black = any('b' in row for row in self.board)
        has_white = any('w' in row for row in self.board)
        if not has_black or not has_white:
            return True  # No pieces left for one player

        # Check if there are any valid moves for any piece
        for y in range(8):
            for x in range(8):
                if self.board[y][x] != '.':
                    if self.valid_moves((x, y)):
                        return False  # Game is not over, moves are still possible

        return True  # No moves left


    def get_all_moves(self, color):
        """ Get all possible moves for a given player color. """
        moves = []
        for y in range(8):
            for x in range(8):
                if self.board[y][x].lower() == color:
                    piece_moves = self.valid_moves((x, y))
                    for move in piece_moves:
                        moves.append(((x, y), move[1]))  # Append start and end positions
        return moves



    def ai_move(self, game):
        _, move = self.minimax(self.board, 3, True, game, float('-inf'), float('inf'))  # depth 3 for simplicity
        return move

