import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(input()))

result = copy.deepcopy(board)

# print(board)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        count = 0
        if board[i][j] == 'X':
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]

                if 0 <= nx < m and 0 <= ny < n:
                    if board[ny][nx] == ".":
                        count += 1
                else:
                    count += 1
            if count >= 3:
                result[i][j] = '.'

# print(result)

start = 0
end = 0
for i in range(n):
    if 'X' in result[i]:
        start = i
        break

for i in range(n-1, -1, -1):
    if 'X' in result[i]:
        end = i
        break

temp = []
for j in range(m):
    for i in range(start, end + 1):
        if 'X' == result[i][j]:
            temp.append(j)
            # break

temp.sort()
for y in range(start, end+1):
    print("".join(result[y][temp[0]:temp[-1]+1]))