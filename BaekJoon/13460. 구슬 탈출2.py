import sys
from collections import deque

n, m = map(int, input().split())

board = list(input() for _ in range(n))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()

visited = [[[[0] * (m) for i in range(n)] for _ in range(m)] for _ in range(n)]


def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by, = i, j
queue.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = 1

while queue:
    rx, ry, bx, by, depth = queue.popleft()

    if depth > 10:
        break

    for k in range(4):
        nrx, nry, rcnt = move(rx, ry, dx[k], dy[k])
        nbx, nby, bcnt = move(bx, by, dx[k], dy[k])

        if board[nbx][nby] != 'O':
            if board[nrx][nry] == 'O':
                print(depth)
                sys.exit(0)
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[k]
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                queue.append((nrx, nry, nbx, nby, depth+1))

print(-1)