def solution(board):
    row = len(board)
    col = len(board[0])

    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] >= 1:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1

    maxn = 0
    for i in range(row):
        maxn = max(maxn, max(board[i]))

    answer = maxn ** 2
    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))