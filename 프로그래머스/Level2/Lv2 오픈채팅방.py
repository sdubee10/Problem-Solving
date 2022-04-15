from collections import defaultdict

def solution(record):
    dict = defaultdict()
    stack = []
    for part in record:
        order = part.split()
        if order[0] == "Enter":
            stack.append((order[1], 1))
            dict[order[1]] = order[2]
        elif order[0] == "Leave":
            stack.append((order[1], 2))
        elif order[0] == "Change":
            dict[order[1]] = order[2]

    answer = []
    for key, value in stack:
        if value == 1:
            answer.append(dict[key] + "님이 들어왔습니다.")
        else:
            answer.append(dict[key] + "님이 나갔습니다.")

    return answer