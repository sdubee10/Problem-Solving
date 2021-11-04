import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.read().split())
graph = [[] for i in range(n + 1)]
ch = [0] * (n + 1)
count = 0

def DFS(L):
    global count
    for vertex in graph[L]:
        if ch[vertex] == 0:
            ch[vertex] = 1
            DFS(vertex)

for i in range(m):
    s, k = map(int, sys.stdin.read().split())
    graph[s].append(k)
    graph[k].append(s)


for i in range(1, n+1):
    if ch[i] == 0:
        ch[i] = 1
        DFS(i)
        count += 1

print(count)