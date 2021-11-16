# n = int(input())
#
# nums = []
# for i in range(n):
#     nums.append(int(input()))
# #answer = []
# for num in nums:
#     for i in range(1, num):
#         if (i**2 + i) >= (2 * num):
#             print(i-1)
#             break
#     if i+1 == num or num == 1:
#         print(1)

import math

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

for num in nums:
    print(math.floor((math.sqrt(1 +(8 * num)) -1)/2))