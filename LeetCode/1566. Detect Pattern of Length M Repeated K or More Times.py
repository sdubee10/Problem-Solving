def solution(arr, m, k):
    answer = False
    n = len(arr)

    tmp = k - 1
    for j in range(n):
        prev = arr[j:j+m]
        for i in range(j+m, n, m):
            next = arr[i:i+m]
            # print("check", prev, next, tmp)
            if prev == next:
                tmp -= 1
                if tmp == 0:
                    return True
            else:
                tmp = k - 1
            prev = next
        tmp = k - 1
        # print("=======")
    return answer

# def containsPattern(arr, m, k):
#         for i in range(len(arr) - m * k + 1):
#             if arr[i: i + m * k] == arr[i: i + m] * k:
#                 return True
#         return False

print(solution([1,2,4,4,4,4], 1, 3))
print(solution([1,2,1,2,1,1,1,3], 2, 2))
print(solution([1,2,1,2,1,3], 2, 3))
print(solution([1,2,3,1,2], 2, 2))
print(solution([2,2,2,2], 2, 3))
print(solution([6,3,5,5,5,5,1,5,6,2,5,1,2,5,3,5,1,3,5,5,6,4,1,2],1,5))
print(solution([3,2,2,1,2,2,1,1,1,2,3,2,2], 3, 2))