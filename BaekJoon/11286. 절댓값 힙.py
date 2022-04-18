import sys
import heapq

input = sys.stdin.readline

h = []

n = int(input())

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(num), num))
