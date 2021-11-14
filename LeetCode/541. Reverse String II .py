def solution(s, k):
    if len(s) < k:
        return s[::-1]
    n = len(s)
    answer = ""
    i = 0
    while (i < n):
        temp = ""
        if i % (2*k) == 0:
            for j in range(i, i+k):
                if i < n:
                    temp += s[j]
                    i += 1
                else:
                    break
            answer += temp[::-1]
        if i < n:
            answer += s[i]
            i += 1
        else:
            break
    return answer

#"bacdfeg"
print(solution("abcdefg",2))

print(solution("abcd", 2))

print(solution("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))