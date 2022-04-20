import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            num = board[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                cnt = 1
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == num:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x-dx[i]][y-dy[i]] == num:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx+dx[i]][ny+dy[i]] == num:
                            break
                        print(num)
                        print(x+1, y+1)
                        sys.exit(0)
                    nx += dx[i]
                    ny += dy[i]
print(0)