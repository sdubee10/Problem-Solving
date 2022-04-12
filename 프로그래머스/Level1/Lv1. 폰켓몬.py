def solution(nums):
    answer = 0
    num = len(nums) // 2
    nums = list(set(nums))
    if len(nums) >= num:
        return num
    else:
        return len(nums)
