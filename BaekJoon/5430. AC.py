import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for i in range(n):
    command = input()
    num = int(input())
    nums = input().rstrip()
    if len(nums) == 2:
        print("error")
        continue

    nums = list(nums[1:-1].split(","))
    queue = deque(nums)

    check = False
    rev = 0
    for letter in command:
        if letter == "R":
            rev += 1
        elif letter == "D":
            if len(queue) > 0:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                check = True
                break
    if check:
        print("error")
    else:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")