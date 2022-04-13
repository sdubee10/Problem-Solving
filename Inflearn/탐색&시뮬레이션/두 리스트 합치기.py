import sys

input = sys.stdin.readline

n = int(input())
numbern = list(map(int, input().split()))

m = int(input())
numberm = list(map(int, input().split()))

answer = []

p1 = p2 = 0

while p1 < n and p2 < m:
    if numbern[p1] < numberm[p2]:
        answer.append(numbern[p1])
        p1 += 1
    else:
        answer.append(numberm[p2])
        p2 += 1
if p1 < n:
    answer = answer + numbern[p1:]
else:
    answer = answer + numberm[p2:]
print(answer)

