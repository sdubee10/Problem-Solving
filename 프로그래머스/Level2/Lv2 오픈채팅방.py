from collections import defaultdict

def solution(record):
    n = len(record)

    dict = defaultdict()

    result = []
    for i in range(n):
        command = record[i].split(" ")
        if command[0] == "Enter":
            dict[command[1]] = command[2]
            result.append((command[1], 1))
        elif command[0] == "Leave":
            result.append((command[1], 2))
        elif command[0] == "Change":
            dict[command[1]] = command[2]

    print(dict)
    print(result)
    answer = []

    for id, value in result:
        if value == 1:
            answer.append(dict[id] + "님이 들어왔습니다.")
        elif value == 2:
            answer.append(dict[id] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))