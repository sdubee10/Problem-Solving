from collections import deque
n, m = map(int, input().split())

board = [i for i in range(101)]
visited = [-1] * 101

for _ in range(n+m):
    x, y = map(int, input().split())
    board[x] = y

queue = deque()
visited[1] = 0
queue.append(1)
while queue:
    now = queue.popleft()
    for i in range(1, 7):
        y = now + i
        if y > 100:
            continue
        y = board[y]
        if visited[y] == -1 or visited[y] > visited[now]+1:
            visited[y] = visited[now] + 1
            queue.append(y)

print(visited[-1])