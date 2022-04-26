import sys

n = int(input())

cnt = 99
if n <= 99:
    print(n)
else:
    for i in range(100, n+1):
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            cnt += 1
    print(cnt)