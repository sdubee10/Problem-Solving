def solution(clothes):
    answer = 1
    dic = {}

    for item in clothes:
        if item[1] in dic:
            dic[item[1]] += [item[0]]
        else:
            dic[item[1]] = [item[0]]

    for i in dic:
        cnt = len(dic[i])
        answer *= (cnt + 1)
    return answer - 1