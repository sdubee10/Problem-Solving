def solution(s):
    stack = []
    n = len(s)
    stack.append(s[0])
    for i in range(1, n):
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    if len(stack):
        return 0
    else:
        return 1


print(solution("baabaa"))
print(solution("cdcd"))