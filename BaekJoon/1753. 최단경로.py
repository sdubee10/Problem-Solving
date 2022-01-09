import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        else:
            for v, w in graph[now]:
                cost = d + w
                if cost < dist[v]:
                    dist[v] = cost
                    heapq.heappush(q, (cost, v))

n, m = map(int, input().split())
s = int(input())
graph = [[]for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(s)

for i in range(1, n+1):
    if dist[i] == sys.maxsize:
        print("INF")
    else:
        print(dist[i])