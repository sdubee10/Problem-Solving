def solution(strings, n):
    answer = list(sorted(sorted(strings), key = lambda x:x[n]))
    return answer