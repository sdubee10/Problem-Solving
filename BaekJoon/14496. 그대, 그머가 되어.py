#dijstra 풀이
"""
import sys
import heapq

input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist_arr = [float('inf')] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dist_arr[a] = 0
q = []
heapq.heappush(q, (0, a))

while q:
    dist, cur = heapq.heappop(q)

    for next in graph[cur]:
        if dist_arr[next] < dist:
            continue
        if dist_arr[next] > dist + 1:
            dist_arr[next] = dist + 1
            heapq.heappush(q, (dist+1, next))

if dist_arr[b] == float('inf'):
    print(-1)
else:
    print(dist_arr[b])
"""

# BFS풀이
"""
import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

queue = deque()
visited[a] = 1
queue.append((0, a))
min_dist = float('inf')

while queue:
    dist, cur = queue.popleft()

    if cur == b:
        min_dist = min(min_dist, dist)
    for next in graph[cur]:
        if not visited[next]:
            visited[next] = 1
            queue.append((dist+1, next))

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)
"""
