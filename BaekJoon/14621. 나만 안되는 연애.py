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

n, m = map(int, input().split())
gender = list(input().split())

parent = [i for i in range(n+1)]
edge = []
for _ in range(m):
    x, y, z = map(int, input().split())
    edge.append((x, y, z))

edge.sort(key = lambda x:x[2])

ans = 0
num = 0

for i in edge:
    a, b, c = i
    if find(a) != find(b) and gender[a-1] != gender[b-1]:
        union(a, b)
        ans += c
        num += 1

if num == n - 1:
    print(ans)
else:
    print(-1)
