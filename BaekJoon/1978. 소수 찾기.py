import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

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

cnt = 0
for num in nums:
    if isPrime(num):
        cnt += 1
print(cnt)