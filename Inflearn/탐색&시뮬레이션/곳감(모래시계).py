import sys

input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
b = [list(map(int, input().split())) for _ in range(m)]

for listb in b:
    h, t, k = listb[0], listb[1], listb[2]
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)