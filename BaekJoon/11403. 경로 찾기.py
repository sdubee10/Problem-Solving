import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def BFS(i, graph, n):
    visit = [0] * n
    q = [i]
    while q:
        index = q.pop(0)
        for i, v in enumerate(graph[index]):
            if visit[i] == 0 and v == 1:
                visit[i] = 1
                q.append(i)
    return visit

for i in range(n):
    print(' '.join(map(str, BFS(i, graph, n))))