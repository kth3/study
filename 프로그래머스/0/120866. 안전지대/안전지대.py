def solution(board):
    n = len(board)
    dir = [(-1, -1), (-1, 0), (-1, 1), 
           (0, -1),           (0, 1), 
           (1, -1),  (1, 0),  (1, 1)]

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                        board[nr][nc] = 2

    return sum(row.count(0) for row in board)