import sys

input = sys.stdin.readline

num = input().rstrip()

m = 0
min, max = '',''

for n in num:
    if n == 'M':
        m += 1
    else:
        if m > 0:
            min += str(10**m + 5)
            max += str(5*(10**m))
        else:
            min += '5'
            max += '5'
        m = 0

if m > 0:
    min += str(10 ** (m-1))
    max += '1' * m

print(max)
print(min)
