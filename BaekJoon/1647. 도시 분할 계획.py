import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(m)]
arr = sorted(arr, key = lambda x:x[2])

unf = [i for i in range(n+1)]

def find(x):
    if x == unf[x]:
        return x
    unf[x] = find(unf[x])
    return unf[x]

def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa != fb:
        unf[fb] = fa

ans = 0

count = 0
for a in arr:
    start, end, c = a
    if find(start) == find(end):
        continue
    else:
        ans += c
        union(start, end)
        count += 1
    if count == n-2:
        break
print(ans)