import sys

input = sys.stdin.readline

m = int(input())
n = int(input())

def isPrime(num):
    if num == 0:
        return False
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return True
ans = []
for i in range(m, n+1):
    if isPrime(i):
        ans.append(i)

if len(ans) != 0:
    print(sum(ans))
    print(ans[0])
else:
    print(-1)