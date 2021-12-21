import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [[-1] * n for i in range(n)]

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

board[r1][c1] = 0
queue = deque()
queue.append((r1, c1))

while queue:
    x, y = queue.popleft()

    for k in range(6):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))
print(board[r2][c2])