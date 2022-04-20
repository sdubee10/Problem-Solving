import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
total = sum(nums)

answer = 0
for num in nums:
    answer += num * (total - num)
    total -= num

print(answer)