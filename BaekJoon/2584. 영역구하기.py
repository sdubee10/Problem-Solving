m, n, k = map(int, input().split())

board = [[0]*(n+1) for i in range(m+1)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()

answer = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = 1
            count = 1
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = 1
                        count += 1
                        queue.append((nx, ny))
            answer.append(count)

print(len(answer))
answer.sort()
print(" ".join(map(str, answer)))