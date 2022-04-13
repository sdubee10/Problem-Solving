import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))

def digit_sum(x):
    num = 0
    while(x>0):
        num += x % 10
        x //= 10
    return num

max = 0
for num in numbers:
    if digit_sum(num) > max:
        max = digit_sum(num)
        res = num

print(res)