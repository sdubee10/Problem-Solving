import sys
input = sys.stdin.readline

a, b = map(int, input().split())
nums = list(map(int, input().split()))

rt = 0
total = 0
result = float('inf')
flag = 0

for lt in range(a):
    while total < b and rt < a:
        total += nums[rt]
        rt += 1

    if total >= b:
        flag = 1
        result = min(result, rt - lt)
    total -= nums[lt]

if flag:
    print(result)
else:
    print(0)