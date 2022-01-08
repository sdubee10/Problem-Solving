import sys

input = sys.stdin.readline

n, k, q, m = map(int, input().split())

k_li = list(map(int, input().split()))

q_li = list(map(int, input().split()))

student = [0] * (n+3)
for i in range(3, n+3):
    student[i] = i

while q_li:
    num = q_li.pop()
    if num not in k_li:
        tmp = num
        while(tmp < n+3):
            if tmp not in k_li:
                student[tmp] = 0
            tmp += num

for _ in range(m):
    a, b = map(int, input().split())
    answer = student[a:b+1].count(0)
    print(b-a - answer+1)