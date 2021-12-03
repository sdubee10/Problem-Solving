n, m = map(int, input().split())

nums = list(map(int, input().split()))

count = 0
for i in range(n):
    total = 0
    for j in range(i, n):
        total += nums[j]
        if total == m:
            count += 1
            break

print(count)