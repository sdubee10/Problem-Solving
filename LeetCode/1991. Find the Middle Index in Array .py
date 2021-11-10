def solution(nums):
    fromleft = [0]
    fromright = [0]

    left = 0
    right = 0
    n = len(nums)
    for i in range(n):
        left += nums[i]
        fromleft.append(left)
        right += nums[n-1-i]
        fromright.insert(0, right)

    fromleft.append(0)
    fromright.insert(0, 0)
    for i in range(1, len(fromleft) -1):
        if fromleft[i-1] == fromright[i+1]:
            return i - 1
    return -1
print(solution([2,3,-1,8,4]))
print(solution([1,-1,4]))
print(solution([2,5]))
print(solution([1]))