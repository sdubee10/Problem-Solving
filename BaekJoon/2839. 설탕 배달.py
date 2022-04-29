import sys

input = sys.stdin.readline
result = 0
n = int(input())

while n >= 0:
    if n % 5 == 0:
        result += n // 5
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)