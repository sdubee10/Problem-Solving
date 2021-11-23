n, m = map(int, input().split())

def DFS(L):
    if L == m:
        print(" ".join(map(str, res)))
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                res[L] = i
                DFS(L+1)

ch = [0] * (n+1)
res = [0] * m
DFS(0)