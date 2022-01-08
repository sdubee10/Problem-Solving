import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        t, now = heapq.heappop(q)

        if time[now] < t:
            continue
        else:
            for v, w in graph[now]:
                cost = t + w
                if cost < time[v] and info[v] == 0:
                    time[v] = cost
                    heapq.heappush(q, (cost, v))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
time = [sys.maxsize] * (n+1)
info = list(map(int, input().split()))
info[-1] = 0
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

dijkstra(0)
if time[n-1] != sys.maxsize:
    print(time[n-1])
else:
    print(-1)

