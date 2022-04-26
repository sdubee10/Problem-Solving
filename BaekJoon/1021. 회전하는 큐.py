import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]
remove = list(map(int, input().split()))
h = deque(nums)

cnt = 0
answer = []
idx = 0
while(len(answer) != m):
    num = remove[idx]
    num_index = h.index(num)
    if num_index == 0 or num_index == len(h) - 1:
        if num_index == 0:
            h.popleft()
        else:
            h.pop()
            cnt += 1
        idx += 1
        answer.append(num)
    else:
        if len(h)//2 - num_index < 0:
            h.insert(0, h.pop())
        else:
            h.append(h.popleft())
        cnt += 1
print(cnt)