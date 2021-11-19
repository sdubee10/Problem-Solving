"""
#두번째 방법

import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
q = []
for _ in range(n):
    row = list(map(int, input().rstrip().split(" ")))
    q.extend(row)
    heapq.heapify(q)

    while(len(q) > n):
        heapq.heappop(q)
print(heapq.heappop(q))

"""


import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
q = []
for _ in range(n):
    q.extend(list(map(int, input().rstrip().split(" "))))
q = heapq.nlargest(n, q)
print(q)
print(q[-1])

heapq.


