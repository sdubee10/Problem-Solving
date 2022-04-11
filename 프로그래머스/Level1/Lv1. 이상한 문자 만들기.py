def solution(s):
    answer = ''

    idx = 0
    for chr in s:
        if chr == ' ':
            idx = -1
            pass
        if idx % 2 == 0:
            answer += chr.upper()
            idx += 1
        else:
            answer += chr.lower()
            idx += 1
    return answer