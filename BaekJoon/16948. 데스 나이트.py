from collections import deque
n = int(input())

r1, c1, r2, c2 = map(int, input().split())
board = [[-1] * n for i in range(n)]
board[r1][c1] = 0

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

queue = deque()
queue.append((r1, c1))
count = 0

while queue:
    x, y = queue.popleft()
    for k in range(6):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= ny < n and 0 <= nx < n and board[nx][ny] == -1:
            queue.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

print(board[r2][c2])