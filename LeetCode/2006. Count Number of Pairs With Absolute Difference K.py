def solution(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if abs(nums[i] - nums[j]) == k:
                count += 1
    return (count)

print(solution([1,2,2,1], 1))
print(solution([1,3], 3))
print(solution([3,2,1,5,4], 2))