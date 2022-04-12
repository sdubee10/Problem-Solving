def solution(d, budget):
    d.sort(reverse=True)
    total = 0
    answer = 0
    while (total <= budget and d):
        total += d.pop()
        if total <= budget:
            answer += 1
    return answer