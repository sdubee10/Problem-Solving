import heapq


def solution(scoville, K):
    food = []
    n = len(scoville)
    count = 0
    for i in range(n):
        heapq.heappush(food, scoville[i])

    while (food[0] < K):
        first = heapq.heappop(food)
        second = heapq.heappop(food)

        newscoville = first + (second * 2)
        heapq.heappush(food, newscoville)
        count += 1

        if len(food) == 1 and food[0] < K:
            return -1
    return count