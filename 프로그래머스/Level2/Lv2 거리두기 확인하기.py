from collections import deque

def bfs(p):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                queue.append((i, j))

                visit = [[0] * 5 for _ in range(5)]
                distance = [[0] * 5 for _ in range(5)]
                visit[i][j] = 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == 0:
                            if p[nx][ny] == 'O':
                                visit[nx][ny] = 1
                                distance[nx][ny] = distance[x][y] + 1
                                queue.append((nx, ny))
                            if p[nx][ny] == "P" and distance[x][y] <= 1:
                                return 0
    return 1


def solution(places):
    answer = []
    for p in places:
        answer.append(bfs(p))
    return answer

print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))