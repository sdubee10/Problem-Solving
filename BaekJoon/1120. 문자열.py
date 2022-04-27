import sys

input = sys.stdin.readline

a, b = map(str, input().split())

lena = len(a)
lenb = len(b)
d = lenb - lena

tmp = float('inf')

for i in range(d+1):
    cnt = 0
    for j in range(lena):
        if a[j] != b[j+i]:
            cnt += 1
    tmp = min(cnt, tmp)

print(tmp)