def solution(msg):

    dict = {}

    for i in range(26):
        dict[chr(ord('A') + i)] = i + 1

    w, c = 0, 0
    index = 27
    answer = []

    while True:
        c += 1
        if c == len(msg):
            answer.append(dict[msg[w:c]])
            break
        if msg[w:c+1] not in dict:
            dict[msg[w:c+1]] = index
            index += 1
            answer.append(dict[msg[w:c]])
            w = c
    return answer