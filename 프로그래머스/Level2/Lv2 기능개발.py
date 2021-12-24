def solution(progresses, speeds):
    answer = []
    result = []
    n = len(progresses)
    for i in range(n):
        check = progresses[i]
        count = 0
        while(check < 100):
            check += speeds[i]
            count += 1
        result.append(count)

    j = 0
    size = len(result)
    temp = result[0]
    count = 0
    while(j < size):
        if temp >= result[j]:
            count += 1
        else:
            temp = result[j]
            answer.append(count)
            count = 1
        j += 1
        if j == size:
            answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print("----------------------------------")
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
