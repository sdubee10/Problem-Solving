# 처음으로 푼 방법:
"""
def solution(s):
    s = list(s)
    n = len(s)
    cnt = 0
    flag = True
    size = 0
    i = 0
    while(i < n):
        if s[i] == "O":
            i += 1
            pass
        elif i + 3 < n:
            if s[i] == "X":
                s[i] = "O"
                flag = False
            elif s[i + 1] == "X":
                s[i + 1] = "O"
                flag = False
            elif s[i + 2] == "X":
                s[i + 2] = "O"
                flag = False

            if flag == False:
                cnt += 1
            i += 3
        else:
            if s[i] == "X":
                s[i] = "O"
            size += 1
            if size == 3:
                cnt += 1
                size = 0
            i += 1
    if 0 < size < 3:
        cnt += 1

    return cnt
"""
#------------------------------------------
# 생각 정리 후...

def solution(s):
    cnt = 0
    n = len(s)
    s = list(s)

    i = 0
    while(i < n):
        if s[i] == "O":
            i += 1
        else:
            cnt +=1
            i += 3
    return cnt

print(solution("XXX"))
print(solution("XXOX"))
print(solution("OOOO"))
print(solution("OXOX"))
print(solution("OXOOX"))