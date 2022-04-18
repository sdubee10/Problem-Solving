from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, value in enumerate(priorities):
        q.append((value, idx))

    while len(q):
        item = q.popleft()

        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer += 1
            if location == item[1]:
                break
    return answer
