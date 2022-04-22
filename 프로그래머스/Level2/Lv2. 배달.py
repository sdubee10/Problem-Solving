import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    dist = [1000] * (N+1)
    answer = 0

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    tree = []
    heapq.heappush(tree, (0, 1))
    dist[1] = 0

    while tree:
        x = heapq.heappop(tree)

        now = x[1]
        now_cost = x[0]

        if now_cost > dist[now]:
            continue
        for nx, nx_cost in graph[now]:
            if now_cost + nx_cost < dist[nx]:
                dist[nx] = now_cost + nx_cost
                heapq.heappush(tree, (dist[nx], nx))
    for i in range(1, N+1):
        if dist[i] <= K:
            answer += 1
    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)