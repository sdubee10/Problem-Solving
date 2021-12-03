
def DFS(L, s):
    if L == 6:
        for i in range(6):
            print(res[i], end = " ")
        print()
        return
    else:
        for i in range(s,nums[0]):
            res[L] = nums[i+1]
            DFS(L+1, i+1)
while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    res = [0] * nums[0]
    DFS(0, 0)
    print("")