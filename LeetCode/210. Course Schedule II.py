from collections import deque
def solution(numCourses, prerequisites):
    graph = [[] for i in range(numCourses)]
    classes = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        classes[a] += 1

    queue = deque()

    for i in range(numCourses):
        if classes[i] == 0:
            queue.append(i)

    answer = []

    while queue:
        now = queue.popleft()
        answer.append(now)

        for i in graph[now]:
            classes[i] -= 1
            if classes[i] == 0:
                queue.append(i)

    if len(answer) == numCourses:
        return answer
    else:
        return []
print(solution(2, [[1,0]]))
# print(solution(4, [[1,0],[2,0], [3,1], [3,2]]))
# print(solution(1, []))

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         graph = [[] for _ in range(numCourses)]
#         inDeg = [0] * numCourses
#         answer = []
#         for [a, b] in prerequisites:
#             graph[a].append(b)
#             inDeg[b] += 1
#         Q = deque()
#         for i in range(numCourses):
#             if inDeg[i] == 0:
#                 Q.append(i)
#         while Q:
#             x = Q.popleft()
#             answer.append(x)
#             for i in graph[x]:
#                 inDeg[i] -= 1
#                 if inDeg[i] == 0:
#                     Q.append(i)
#         return answer[::-1] if len(answer) == numCourses else []