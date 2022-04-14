import sys

input = sys.stdin.readline

nums = []
for _ in range(9):
    nums.append(int(input()))

total = sum(nums)

flag = False
for i in range(9):
    first = nums[i]
    for j in range(i+1, 9):
        second = nums[j]
        if total - nums[i] - nums[j] == 100:
            flag = True
            break
    if flag == True:
        break
nums.remove(first)
nums.remove(second)
nums.sort()
for i in range(7):
    print(nums[i])
