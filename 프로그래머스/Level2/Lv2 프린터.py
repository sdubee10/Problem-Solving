from collections import deque

def solution(priorities, location):
    answer = 0

    queue = deque()
    for idx, value in enumerate(priorities):
        queue.append((value, idx))

    while len(queue):
        item = queue.popleft()

        if queue and max(queue)[0] > item[0]:
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))