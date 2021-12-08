import sys

input = sys.stdin.readline

n = int(input())

def isPrime(num):
    if num < 2 :
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check(num):
    strnum = str(num)
    n = len(strnum)

    for i in range(n//2):
        if strnum[i] != strnum[n - i-1]:
            return False
    return True

while True:
    if check(n):
        if isPrime(n):
            print(n)
            break
    n += 1