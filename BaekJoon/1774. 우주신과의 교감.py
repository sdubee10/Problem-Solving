import sys
import math

def Find(x):
   if p[x] == x:
      return x
   else:
      y = Find(p[x])
      p[x] = y
      return y


def Union(x, y):
   x = Find(x)
   y = Find(y)
   if x != y:
      p[y] = x


n, m = map(int, sys.stdin.readline().split())

p = [i for i in range(n)]


location = []
for _ in range(n):
   x, y = map(int, sys.stdin.readline().split())
   location.append([x, y])

count = 0
for _ in range(m):
   god1, god2 = map(int, sys.stdin.readline().split())
   if Find(god1 - 1) != Find(god2 - 1):
      Union(god1 - 1, god2 - 1)
      count += 1

road = []
for i in range(n - 1):
   for j in range(i + 1, n):
      dis = math.sqrt((location[i][0] - location[j][0]) ** 2 + (location[i][1] - location[j][1]) ** 2)
      road.append([dis, i, j])

road.sort(key=lambda x: x[0])

answer = 0
for dis, x, y in road:
   if Find(x) != Find(y):
      Union(x, y)
      answer += dis
      count += 1
   if count == n - 1:
      break

print(round(answer, 2))