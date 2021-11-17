def solution(arr):
    answer = True
    arr.sort()
    diff = arr[1] - arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] - arr[i-1] != diff:
            return False
    return answer

print(solution([3,5,1]))