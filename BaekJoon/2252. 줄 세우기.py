from collections import deque

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
people = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    people[b] += 1

queue = deque()
result = []

for i in range(1, n+1):
    if people[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)
    for i in graph[now]:
        people[i] -= 1
        if people[i] == 0:
            queue.append(i)

tmp = " ".join(map(str, result))
print(tmp)