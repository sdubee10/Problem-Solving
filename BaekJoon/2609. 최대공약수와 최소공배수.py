import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


gcdn = gcd(a, b)
print(gcdn)
print((a * b) // gcdn)