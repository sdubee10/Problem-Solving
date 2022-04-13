import sys

input = sys.stdin.readline

n = int(input())
answer = list(map(int, input().split()))

cnt = 0
sum = 0
for x in answer:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)