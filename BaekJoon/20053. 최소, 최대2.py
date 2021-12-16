import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    m = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[0], nums[-1])