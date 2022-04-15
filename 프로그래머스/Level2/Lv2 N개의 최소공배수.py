def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer = answer * arr[i] / gcd(answer, arr[i])
    return answer