n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ch = [0] * (n+1)
res = [0] * m
result = set()

def DFS(L):
    if L == m:
        tmp = " ".join(map(str, res))
        if tmp not in result:
            result.add(tmp)
            print(tmp)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = nums[i-1]
                DFS(L+1)
                ch[i] = 0
DFS(0)