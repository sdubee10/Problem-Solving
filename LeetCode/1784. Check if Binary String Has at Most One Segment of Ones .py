def solution(s):
    for i in range(1, len(s)):
        if s[i - 1] == '0' and s[i] == '1':
            return False
    return True

print(solution("1001"))
print(solution("110"))