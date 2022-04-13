import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def check_prime(num):
    if num == 0:
        return 0
    tmp = 0
    flag = True
    while(num > 0):
        tmp = tmp * 10 + num % 10
        num //= 10

    for i in range(2, int(tmp ** 0.5) + 1):
        if tmp % i == 0:
            flag = False

    if flag == True:
        return tmp
    else:
        return 0

answer = []
for num in nums:
    if check_prime(num) != 0:
        answer.append(check_prime(num))

print(answer)