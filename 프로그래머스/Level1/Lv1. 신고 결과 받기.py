def solution(id_list, report, k):
    answer = []
    user = {}
    count = {}
    for id in id_list:
        user[id] = []
        count[id] = 0

    for case in set(report):
        a, b = case.split()
        user[a].append(b)
        count[b] += 1

    for key, value in user.items():
        check = 0
        for name in value:
            if count[name] >= k:
                check += 1
        answer.append(check)

    return answer