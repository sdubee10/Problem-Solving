# 1-1 = 1
# 2-(1,1), 2 = 2
# 3-(1,1,1),(2,1), 3 = 3
# 4=(1,1,1,1), (2,1,1), (2,2), (1,3) = 4
# 5=(1,1,1,1,1),(2,2,1), (2,3), (2,1,1,1), (3,1,1) = 5
# 6=(1,1,1,1,1,1), (1,1,1,1,2),(1,1,2,2),(2,2,2),(1,1,1,3),(3,3),(2,3,1) = 7
# 7=(1,1,1,1,1,1,1), (1,1,1,1,1,2), (1,1,1,2,2), (1,2,2,2), (1,1,1,1,3), (1,3,3)
# (2,2,3), (2,3,1,1) = 8
#
# 1,2,3,4,5,6,7
# 1,2,3,4,5,7,8


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

dp = [0 for _ in range(10001)]
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 3

for i in range(4, 10001):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3])
    if i % 3 == 0:
        dp[i] += 1

for i in a:
    print(dp[i])