import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

nxt = [i for i in range(101)]
check = [-1] * (101)

for i in range(n + m):
    x, y = map(int, input().split())
    nxt[x] = y

queue = deque()
check[1] = 0
queue.append(1)

while queue:
    now = queue.popleft()

    for i in range(1, 7):
        move = now + i
        if move <= 100:
            move = nxt[move]
            if check[move] == -1 or check[move] > check[now] + 1:
                check[move] = check[now] + 1
                queue.append(move)
print(check[-1])
