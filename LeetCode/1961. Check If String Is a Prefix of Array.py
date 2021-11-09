def solution(s, words):
    n = len(words)
    tmp =""
    for i in range(n):
        tmp += words[i]
        if s == tmp:
            return True
    return False

print(solution("iloveleetcode", ["i","love","leetcode","apples"])) #True
print(solution("iloveleetcode", ["apples","i","love","leetcode"])) #False