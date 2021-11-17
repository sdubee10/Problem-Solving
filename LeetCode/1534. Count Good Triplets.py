def solution(arr, a, b, c):
    answer = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        answer += 1
    return answer

print(solution([3,0,1,1,9,7], 7, 2, 3))

print(solution([1, 1, 2, 2, 3], 0, 0, 1))