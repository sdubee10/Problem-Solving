import sys

input = sys.stdin.readline

n = int(input())

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(n):
    num = int(input())
    while(isPrime(num) == False):
        num += 1
    print(num)
