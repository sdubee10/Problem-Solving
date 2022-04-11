def solution(n):
    n = int(n)
    answer = list(str(n))
    answer.sort(reverse = True)
    return int(''.join(answer))