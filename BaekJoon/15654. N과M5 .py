n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def DFS(L):
    if L == m:
        print (" ".join(map(str, res)))
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = nums[i]
                DFS(L+1)
                ch[i] = 0
ch = [0] * (n+1)
res = [0] * m


DFS(0)

