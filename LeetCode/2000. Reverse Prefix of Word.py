def solution(word, ch):
    check = True
    for i in range(len(word)):
        if word[i] == ch:
            check = False
            break
    if check == True:
        return word
    else:
        answer = word[:i+1][::-1] + word[i+1:]
        return answer

print(solution("abcdefd", "d"))
print(solution("xyxzxe", "z"))
print(solution("abcd", "z"))
print(solution("rzwuktxcjfpamlonbgyieqdvhs", "s"))