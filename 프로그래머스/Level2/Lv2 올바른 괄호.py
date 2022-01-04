def solution(s):
    n = len(s)
    stack = []
    for i in range(n):
        if i == 0 and s[i] == ")":
            return False
        else:
            if stack and s[i] == ")":
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
