def trinary(n):
    list = []
    while(n > 0):
        list.append(n % 3)
        n //= 3
    return list[::-1]

def convert(s):
    base = 1
    answer = 0
    for i in range(len(s)):
        answer += base * s[i]
        base = base * 3
    return answer

def solution(n):
    answer = convert(trinary(n))
    return answer