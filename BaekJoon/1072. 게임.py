import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

score = (m * 100 // n)
if score >= 99:
    print(-1)
    sys.exit(0)

left = 1
right = n
count = 0

while left <= right:
    mid = (left + right)//2

    if (m+mid) *100 // (n + mid) <= score:
        left = mid + 1
    else:
        count = mid
        right = mid - 1

print(count)