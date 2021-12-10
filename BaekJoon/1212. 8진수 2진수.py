import sys

input = sys.stdin.readline

n = int(input(), 8)

answer = bin(n)
print(answer[2:])