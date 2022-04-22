import sys

input = sys.stdin.readline

n, m = map(int, input().split())

days = []
num = 0
for _ in range(n):
    days.append(int(input()))

for i in range(n - 1):
    if days[i] < days[i+1]:
        if m // days[i] > 0:
            num = m // days[i]
            m = m-(num * days[i])
    elif days[i] > days[i+1]:
        m += num * days[i]
        num = 0
if num > 0:
    m += num * days[-1]
print(m)
