from collections import deque
def solution(numCourses, prerequisites):
    graph = [[] for i in range(numCourses)]
    classes = [0] * numCourses

    for a, b in prerequisites:
        graph[a].append(b)
        classes[b] += 1

    queue = deque()

    for i in range(numCourses):
        if classes[i] == 0:
            queue.append(i)

    cnt = 0
    while queue:
        now = queue.popleft()
        cnt += 1
        for i in graph[now]:
            classes[i] -= 1
            if classes[i] == 0:
                queue.append(i)

    return cnt == numCourses

print(solution(2, [[1,0]]))
print(solution(2, [[1,0],[0, 1]]))

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = [[] for _ in range(numCourses)]
#         inDeg = [0] * numCourses
#         cnt = 0
#         for [a, b] in prerequisites:
#             graph[a].append(b)
#             inDeg[b] += 1
#         Q = deque()
#         for i in range(numCourses):
#             if inDeg[i] == 0:
#                 Q.append(i)
#         while Q:
#             x = Q.popleft()
#             cnt += 1
#             for i in graph[x]:
#                 inDeg[i] -= 1
#                 if inDeg[i] == 0:
#                     Q.append(i)
#         return cnt == numCourses
