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


n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]
edges = []
location = [[]]

for _ in range(n):
   x, y = map(int, input().split())
   location.append((x, y))

count = 0
for _ in range(m):
   x, y = map(int, input().split())
   if find(x) != find(y):
      union(x, y)
      count += 1

for i in range(1, n):
   for j in range(i+1, n+1):
      d = math.sqrt((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1])**2)
      edges.append((i, j, d))

# print(edges)
edges.sort(key = lambda x:x[2])
# print("$"*10)
# print(edges)
ans = 0
for edge in edges:
   x, y, d = edge
   if find(x) != find(y):
      union(x, y)
      ans += d
      count += 1
   if count == n-1:
      break

print("%.2f" % ans)