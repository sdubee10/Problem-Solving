import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

mean = round(sum(a)/n)
tmp = float('inf')
ans = 0
for i in range(n):
    if abs(a[i] - mean) < tmp:
        tmp = abs(a[i] - mean)
        score = a[i]
        ans = i + 1
    elif abs(a[i] - mean) == tmp:
        if score < a[i]:
            score = a[i]
            ans = i + 1

print(mean, ans)

