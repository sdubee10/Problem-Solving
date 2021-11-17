def solution(prices):
    answer = []
    n = len(prices)
    for i in range(1,n):
        for j in range(i, n):
            if prices[j] <= prices[i-1]:
                answer.append(prices[i-1] - prices[j])
                break
        else:
            answer.append(prices[i-1])
    answer.append(prices[-1])
    return answer

print(solution([8,4,6,2,3]))

print(solution([1,2,3,4,5]))

print(solution([10,1,1,6]))
