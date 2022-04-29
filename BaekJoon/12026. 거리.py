n = int(input())
block = input().rstrip()

dp = [float('inf')] * (n+1)

def get_prev(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"

dp[0] = 0
for i in range(1, n):
    prev = get_prev(block[i])
    for j in range(i):
        if block[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))
        print(dp, dp[i], i, j, block[j], prev)
print(dp[n - 1] if dp[n - 1] != float('inf') else -1)