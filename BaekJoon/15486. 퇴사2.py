import sys

input = sys.stdin.readline

n = int(input())
time = []
pay = []
dp = [0] * (n+1)

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    pay.append(b)

for i in range(n):
    if time[i] <= n-i:
        dp[i+time[i]] = max(dp[i+time[i]], dp[i] + pay[i])

    dp[i + 1] = max(dp[i+1], dp[i])

print(dp[n])