n, m = map(int, input().split())

def DFS(L, s):
    if L == m:
        print(" ".join(map(str, res)))
    else:
        for i in range(s, n+1):
            if ch[i] == 0:
                res[L] = i
                DFS(L+1, i)
ch = [0] * (n+1)
res = [0] * m

DFS(0, 1)