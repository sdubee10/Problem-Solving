# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# nums = []
# for i in range(n):
#     nums.append(float(input()))
#
# for i in range(1, n):
#     nums[i] = max(nums[i], nums[1-i]*nums[i])
#
# print(round(max(nums), 3))

N = int(input())
nums = [float(input()) for _ in range(N)]
for i in range(1, N):
    nums[i] = max(nums[i - 1] * nums[i], nums[i])
print("{:.3f}".format(max(nums)))