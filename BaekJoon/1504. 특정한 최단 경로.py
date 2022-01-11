import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
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
    return dist
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, e = map(int, input().split())

start = dijkstra(1)
v1 = dijkstra(s)
v2 = dijkstra(e)

answer = min(start[s]+v1[e]+v2[n], start[e] + v2[s] + v1[n])

print(answer if answer < sys.maxsize else -1)