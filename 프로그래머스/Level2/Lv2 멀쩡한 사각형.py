import math
def solution(w,h):
    gcd = math.gcd(w,h)
    a = w // gcd
    b = h // gcd
    return w * h - (a+b - 1) *gcd

print(solution(8, 12))