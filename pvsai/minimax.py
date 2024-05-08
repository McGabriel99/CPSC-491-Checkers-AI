def evaluate_board(board):
    score = 0
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece == 'b':
                score += 5
            elif piece == 'B':  # King
                score += 10
            elif piece == 'w':
                score -= 5
            elif piece == 'W':  # King
                score -= 10
    return score

def minimax(board, depth, maximizingPlayer, game, alpha, beta):
    if depth == 0:
        return evaluate_board(board), None

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for y in range(8):
            for x in range(8):
                if board[y][x].lower() == 'b':
                    moves = game.valid_moves((x, y))
                    for move in moves:
                        game.make_move(move[0], move[1])
                        eval, _ = minimax(board, depth - 1, False, game, alpha, beta)
                        game.undo_move(move[1], move[0], board)
                        if eval > maxEval:
                            maxEval = eval
                            best_move = move
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for y in range(8):
            for x in range(8):
                if board[y][x].lower() == 'w':
                    moves = game.valid_moves((x, y))
                    for move in moves:
                        game.make_move(move[0], move[1])
                        eval, _ = minimax(board, depth - 1, True, game, alpha, beta)
                        game.undo_move(move[1], move[0], board)
                        if eval < minEval:
                            minEval = eval
                            best_move = move
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
        return minEval, best_move
