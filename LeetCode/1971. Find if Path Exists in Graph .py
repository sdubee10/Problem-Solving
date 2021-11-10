from collections import deque
import collections
def solution(n, edges, start, end):
    answer = False
    graph = [[] for _ in range(n+1)]

    # graph = collections.defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = set()
    #print(graph)
    q = deque()
    q.append(start)
    #print(q)
    while q:
        c = q.popleft()

        if c == end:
            return True

        for nx in graph[c]:
            if nx not in visited:
                q.append(nx)
        visited.add(c)

    return answer

# print(solution(3, [[0,1],[1,2],[2,0]], 0, 2))
print(solution(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))





