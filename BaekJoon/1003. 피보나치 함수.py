n = int(input())
answer = []

nums = []
for i in range(n):
    nums.append(int(input()))

maxnum = max(nums)
dp = [0] * (maxnum+1)

if maxnum != 0:
    dp[1] = 1
dp[0] = 0

for j in range(2, maxnum+1):
    dp[j] = dp[j-1] + dp[j-2]

for num in nums:
    if num == 0:
        print(1, 0)
    else:
        print(dp[num-1], dp[num])