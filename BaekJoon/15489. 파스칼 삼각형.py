import sys

input = sys.stdin.readline

r, c, w = map(int, input().split())

board = [[0] * 30 for _ in range(30)]

for i in range(30):
    j = 0
    while(j <= i):
        if j == 0 or j == i:
            board[i][j] = 1
        else:
            if 1 <= j < i and i > 1:
                board[i][j] = board[i-1][j-1] + board[i-1][j]
        j += 1

triangle = 0
idx = 0

for i in range(r-1, r+w -1):
    for j in range(c-1, c+idx):
        triangle += board[i][j]
    idx += 1

print(triangle)