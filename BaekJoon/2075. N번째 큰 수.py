import sys
import heapq

n = int(input())

num = []
for _ in range(n):
    tmp = list(map(int, input().rstrip().split()))
    num.extend(tmp)
    heapq.heapify(num)

    while (len(num) > n):
        heapq.heappop(num)

print(heapq.heappop(num))