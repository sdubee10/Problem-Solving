from collections import deque


def solution(cacheSize, cities):
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer

    answer = 0
    lru = deque()
    for i in range(cacheSize):
        if cities[i] in lru:
            if len(lru) == cacheSize:
                lru.remove(cities[i])
                lru.append(cities[i])
            else:
                lru.append(cities[i])
            answer += 1
        else:
            lru.append(cities[i])
            answer += 5
    for i in range(cacheSize, len(cities)):
        if cities[i] in lru:
            lru.remove(cities[i])
            lru.append(cities[i])
            answer += 1
        else:
            temp = lru.popleft()
            lru.append(cities[i])
            answer += 5

    return answer