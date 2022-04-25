import sys

input = sys.stdin.readline

n, m = map(int, input().split())

global count
count = 0
def DFS(total, tmp):
    global count
    if total > n:
        return
    if total == n:
        count += 1
        if count == m:
            print(tmp[:-1])
            sys.exit(0)
    for i in range(1, 4):
        DFS(total + i, tmp + str(i) + "+")
DFS(0, "")
print(-1)
