import sys
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(s):
    q = deque()
    q.append(s)

    visited = [0 for _ in range(n+1)]
    visited[s] = 1

    while q:
        x = q.popleft()

        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[x] + 1
                q.append(i)
bfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)