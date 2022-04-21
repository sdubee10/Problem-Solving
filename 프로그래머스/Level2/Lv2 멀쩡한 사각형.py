def gcd(w, h):
    if w % h == 0:
        return h
    else:
        return gcd(h, w % h)

def solution(w,h):
    num = gcd(w,h)
    a = w // num
    b = h // num
    # print(a, b)
    # print(num)
    return w * h - (a+b - 1) *num

