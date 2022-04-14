import sys
input = sys.stdin.readline

maxn = -2147000000
curr= 0
for _ in range(10):
    n, m = map(int, input().split())
    curr = curr + m - n

    if curr > maxn:
        maxn = curr
print(maxn)