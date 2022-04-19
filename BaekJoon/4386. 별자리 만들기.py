import sys
import math

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
edge = []
stars = []
ans = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        edge.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edge.sort()

for i in edge:
    cost, x, y = i

    if find(x) != find(y):
        union(x, y)
        ans += cost

print(round(ans, 2))