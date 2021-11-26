from collections import deque
n, m = map(int, input().split())

queue = deque()
for i in range(1, n+1):
    queue.append(i)

k = 1
result=[]
while(len(queue) != 1):
    if k == m:
        result.append(queue.popleft())
        k = 0
    else:
        queue.append(queue.popleft())
    k += 1

result.append(queue.popleft())

print("<"+", ".join(map(str, result))+">")