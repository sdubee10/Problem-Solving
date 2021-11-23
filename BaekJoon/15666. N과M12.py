n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ch = [0] * (n+1)
res = [0] * m
result = set()

def DFS(L, s):
    if L == m:
        tmp = " ".join(map(str, res))
        if tmp not in result:
            result.add(tmp)
            print(tmp)
        return
    else:
        for i in range(s, n):
            res[L] = nums[i]
            DFS(L+1, i)
            res[L] = 0

DFS(0, 0)