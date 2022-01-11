import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    x = q.popleft()

    if x == m:
        print(visited[x])
        break
    if 0 <= x -1 < 100001 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if 0 <= 2 * x < 100001 and visited[2*x] == -1:
        visited[2*x] = visited[x]
        q.append(2*x)
    if 0 <= x + 1 < 100001 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)