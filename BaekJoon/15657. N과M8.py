n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ch = [0] * (n+1)
res = [0] * m

def DFS(L, s):
    if L == m:
        print(" ".join(map(str, res)))
    else:
        for i in range(s, n+1):
            res[L] = nums[i-1]
            DFS(L+1, i)

DFS(0, 1)
