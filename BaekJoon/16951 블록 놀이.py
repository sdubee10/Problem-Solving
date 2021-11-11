n,k = map(int, input().split())

nums = list(map(int, input().split()))

answer = n
for i in range(n):
    tres = 0
    for j in range(n):
        now = (j-i) * k + nums[i]
        if now < 1:
            tres = n
            break
        if now != nums[j]:
            tres += 1
    answer = min(answer, tres)

print(answer)