def solution(lottos, win_nums):
    count = 0
    for i in range(len(lottos)):
        for j in range(len(lottos)):
            if lottos[i] == win_nums[j]:
                count += 1
    zero = lottos.count(0)
    if zero == 6:
        answer = [7 - count - zero, 6]
    elif count == 0 and zero == 0:
        answer = [6, 6]
    else:
        answer = [7 - count - zero, 7 - count]
    return answer