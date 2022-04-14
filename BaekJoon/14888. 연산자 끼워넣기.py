n = int(input())

nums = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

maxnum = -1e9
minnum = 1e9

def DFS(cnt, res, add, sub, mul, div):
    global maxnum
    global minnum

    if cnt == n:
        maxnum = max(maxnum, res)
        minnum = min(minnum, res)
        return

    else:
        if add:
            DFS(cnt + 1, res + nums[cnt], add - 1, sub, mul, div)
        if sub:
            DFS(cnt + 1, res - nums[cnt], add, sub - 1, mul, div)
        if mul:
            DFS(cnt + 1, res * nums[cnt], add, sub, mul - 1, div)
        if div:
            DFS(cnt + 1, int(res / nums[cnt]), add, sub, mul, div - 1)

DFS(1, nums[0], add, sub, mul, div)
print(maxnum)
print(minnum)