import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
start = int(input()) -1

ch = [0] * (n+1)

queue = deque()
queue.append(start)

while queue:
    now = queue.popleft()
    ch[now] = 1
    for jump in [-stones[now], stones[now]]:
        move = now + jump
        if 0 <= move < n and ch[move] == 0:
            ch[move] = 1
            queue.append(move)

print(ch.count(1))