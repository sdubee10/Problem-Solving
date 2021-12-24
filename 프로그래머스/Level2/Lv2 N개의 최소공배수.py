def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer = (arr[i] * answer) // (gcd(arr[i], answer))
    return answer
print(solution([2,6,8,14]))
print(solution([1,2,3]))
