def solution(s):
    s = s.split(" ")
    n = len(s)
    for i in range(n):
        s[i] = int(s[i])
    s.sort()
    answer = str(s[0]) + " " + str(s[n-1])
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))