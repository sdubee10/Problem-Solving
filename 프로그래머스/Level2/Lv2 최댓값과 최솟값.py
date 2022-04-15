def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = int(s[i])
    s.sort()

    return str(s[0]) + " " + str(s[len(s) - 1])