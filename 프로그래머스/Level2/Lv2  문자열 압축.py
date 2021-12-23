def solution(s):
    answer = float('inf')
    n = len(s)

    for i in range(1, n//2+1):
        result = ""
        count = 1
        temp = s[:i]
        for j in range(i, n*2, i):
            #print(s[j:j+i])
            if temp == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp
                    count = 1
                temp = s[j:j+i]
        answer = min(answer, len(result))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
# "aabbaccc"	7
# "ababcdcdababcdcd"	9
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd" 17