def solution(x):
    check = 0
    tmp = x
    while(tmp > 0):
        check += tmp % 10
        tmp //= 10
    if x % check == 0:
        return True
    else:
        return False