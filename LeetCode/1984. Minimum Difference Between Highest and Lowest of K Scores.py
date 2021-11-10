def solution(nums, k):
    if k == 1:
        return 0

    left = 0
    right = k - 1
    answer = float('inf')
    nums.sort()
    while(right < len(nums)):
        answer = min(answer, abs(nums[left] - nums[right]))
        left += 1
        right += 1
    return answer

print(solution([90], 1))
print(solution([9,4,1,7], 2))
print(solution([87063,61094,44530,21297,95857,93551,9918], 6))