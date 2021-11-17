def solution(nums):
    answer = []
    n = len(nums)
    total = 0
    for i in range(n):
        total += nums[i]
        answer.append(total)

    return answer

print(solution([1,2,3,4]))
print(solution([1, 1, 1, 1, 1]))