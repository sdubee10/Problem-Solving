def solution(participant, completion):
    start = {}
    for people in participant:
        if people not in start:
            start[people] = 1
        else:
            start[people] += 1

    for people in completion:
        start[people] -= 1

    for key, value in start.items():
        if value == 1:
            return key