def solution(nums):
    nums = set(nums)
    nums = list(nums)
    nums.sort(reverse = True)
    if len(nums) < 3:
        return max(nums)
    else:
        return nums[2]

print(solution([3,2,1]))
print(solution([1,2]))