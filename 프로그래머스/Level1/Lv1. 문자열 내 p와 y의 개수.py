def solution(s):
    answer = True
    s = s.lower()
    countp = 0
    county = 0
    for i in range(len(s)):
        if s[i] == 'p':
            countp += 1
        elif s[i] == 'y':
            county += 1

    if countp == 0 and county == 0:
        return True
    elif countp == county:
        return True
    else:
        return False
