from collections import deque

n, m = map(int, input().split())

board = [i for i in range(101)]
dist = [-1] * 101

for _ in range(n+m):
    x, y = map(int,input().split())
    board[x] = y

queue = deque()
dist[1] = 0
queue.append(1)

while queue:
    now = queue.popleft()
    for i in range(1, 7):
        y = now + i
        if y > 100:
            continue
        y = board[y]
        if dist[y] == -1 or dist[y] > dist[now] + 1:
            dist[y] = dist[now] + 1
            queue.append(y)
print(dist[-1])