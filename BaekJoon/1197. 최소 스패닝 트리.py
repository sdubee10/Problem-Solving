import sys

n, m = map(int, input().split())

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


edge = []
parent = [i for i in range(n+1)]
ans = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    edge.append((x, y, z))

edge.sort(key = lambda x:x[2])
for i in edge:
    x, y, z = i
    if find(x) != find(y):
        union(x, y)
        ans += z
        print(ans)

print(ans)