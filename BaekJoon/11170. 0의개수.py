import sys

input = sys.stdin.readline

n = int(input())

result = []
for i in range(n):
    a, b= map(int, input().split())
    count = 0
    for i in range(a, b+1):
        for num in str(i):
            if num == "0":
                count += 1
    result.append(count)

for i in range(n):
    print(result[i])