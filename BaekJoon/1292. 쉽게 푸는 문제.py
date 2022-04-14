import sys

input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 1
nums = []
while  cnt < 1000:
    for _ in range(cnt):
        nums.append(cnt)
    cnt += 1

print(sum(nums[a-1:b]))