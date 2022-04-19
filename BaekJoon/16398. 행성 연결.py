import sys

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
parent = [i for i in range(n+1)]
graph = [list(map(int, input().split())) for _ in range(n)]

edges = []
for a in range(n):
    for b in range(a+1, n):
        edges.append((graph[a][b], a, b))

edges.sort()
res = 0
for edge in edges:
    c, x, y = edge
    if find(x) != find(y):
        union(x, y)
        res += c
print(res)