import sys
from collections import deque

n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = []
for _ in range(m):
    board.append(input())

dist = [[-1] * n for _ in range(m)]

q = deque()
q.append((0,0))
dist[0][0] = 0

while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
            if board[nx][ny] == "0":
                q.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]
            elif board[nx][ny] == "1":
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

print(dist[m-1][n-1])