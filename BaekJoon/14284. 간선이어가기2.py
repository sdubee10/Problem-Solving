import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
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
graph = [[] for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())
dijkstra(s)
print(dist[t])