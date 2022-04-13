import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

answer = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            answer.add(a[i] + a[j] + a[m])
answer = list(answer)
answer.sort(reverse=True)
print(answer[k-1])
