import sys
import heapq

input = sys.stdin.readline

def check(data):
    n = len(data)
    left = []
    right = []
    middle = data[0]
    result = [middle]

    for idx, value in enumerate(data[1:], 1):
        if value > middle:
            heapq.heappush(right, value)
        else:
            heapq.heappush(left, -value)

        if idx % 2 == 0:
            if len(left ) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            result.append(middle)
    print(len(result))
    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()

n = int(input())
for _ in range(n):
    m = int(input())

    nums = []
    if m % 10 == 0:
        for _ in range(m // 10):
            nums.extend(list(map(int, input().split())))
    else:
        for _ in range(m // 10 + 1):
            nums.extend(list(map(int, input().split())))

    check(nums)