import sys

input = sys.stdin.readline

h, w = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = w - 1

res = 0
maxleft = nums[left]
maxright = nums[right]

while left < right:
    maxleft = max(maxleft, nums[left])
    maxright = max(maxright, nums[right])

    if maxright > maxleft:
        res += maxleft - nums[left]
        left += 1
    else:
        res += maxright - nums[right]
        right -= 1

print(res)