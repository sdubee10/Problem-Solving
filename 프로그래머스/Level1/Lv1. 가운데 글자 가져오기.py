def solution(s):
    l = len(s)
    if l % 2 == 0 :
        return s[int(l/2) - 1 : int(l/2)+1]
    else:
        return s[int(l/2)]