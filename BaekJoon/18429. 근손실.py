import sys

input = sys.stdin.readline
n, k = map(int, input().split())

nums = list(map(int, input().split()))

ch = [0] * (n+1)
global count
count = 0

def DFS(L, total):
    global count
    if total < 500:
        return
    if L == n:
        count += 1
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                DFS(L + 1, total + nums[i] - k)
                ch[i] = 0
DFS(0, 500)
print(count)
