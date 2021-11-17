def solution(n, rounds):
    sector = [i for i in range(1, n+1)]
    count = [0] * (n+1)
    size = len(rounds)

    count[rounds[0]] += 1
    for i in range(1, size):
        j = rounds[i-1] + 1
        if j <= rounds[i]:
            while(j <= rounds[i]):
                count[j] += 1
                j += 1
            # print("1st", count, j, i)
        else:
            while(j <= sector[n-1]):
                count[j] += 1
                j += 1
            j = sector[0]
            while(j <= rounds[i]):
                count[j] += 1
                j += 1

    big = max(count)
    answer = []
    for i in range(n+1):
        if count[i] == big:
            answer.append(i)
    return answer

print(solution(4, [1,3,1,2]))
print(solution(2, [2,1,2,1,2,1,2,1,2]))
print(solution(7, [1, 3, 5, 7]))
