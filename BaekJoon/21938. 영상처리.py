import sys
from collections import deque

n, m = map(int, input().split())

monitor = []

for i in range(n):
    monitor.append(list(map(int, input().split())))

limit = int(input())

newmonitor = [[0] * (m) for i in range(n)]

for i in range(n):
    for j in range(m):
        avg = (monitor[i][3*j+1] + monitor[i][3*j+2] + monitor[i][3*j]) // 3
        newmonitor[i][j] = avg

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit = [[0] * (m) for i in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if newmonitor[i][j] >= limit and visit[i][j] == 0:
            queue = deque()
            queue.append((i, j))
            visit[i][j] = 1

            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and newmonitor[nx][ny] >= limit:
                        visit[nx][ny] = 1
                        queue.append((nx, ny))
            cnt += 1
print(cnt)