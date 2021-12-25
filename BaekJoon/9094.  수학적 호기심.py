#pypy3
import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, m = map(int, input().split())
    count = 0
    for i in range(1, a-1):
        for j in range(i+1,a):
            temp = i ** 2 + j ** 2 + m
            if temp % (i * j) == 0:
                count += 1
    print(count)


"""
#python
from itertools import *
for _ in range(int(input())):
  n, m = map(int, input().split())
  print(sum((a*a+b*b+m)%(a*b) == 0 for a, b in combinations(range(1, n), 2)))
"""
