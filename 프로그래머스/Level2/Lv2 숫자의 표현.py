def solution(n):
    b = 1
    a = n - b
    cnt = 0
    while (a > 0):
        b += 1
        a -= b
        if a % b == 0:
            cnt += 1
    return cnt + 1