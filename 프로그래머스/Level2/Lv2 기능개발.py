def solution(progresses, speeds):
    days = []
    for i in range(len(speeds)):
        count = 0
        while (progresses[i] < 100):
            progresses[i] = progresses[i] + speeds[i]
            count += 1
        days.append(count)

    idx = 0
    tmp = days[0]
    answer = []
    count = 0
    while (idx < len(days)):
        if tmp >= days[idx]:
            count += 1
        else:
            tmp = days[idx]
            answer.append(count)
            count = 1
        idx += 1
    answer.append(count)
    return answer