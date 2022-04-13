def solution(new_id):
    new_id = new_id.lower()

    answer = ''
    for chr in new_id:
        if chr in ['_', '-', '.'] or chr.isnumeric() or chr.islower():
            answer += chr

    tmp = ''
    for i in range(1, len(answer)):
        if answer[i - 1] == '.' and answer[i] == '.':
            pass
        else:
            tmp += answer[i - 1]

    tmp += answer[-1]
    tmp = tmp.replace("..", ".")
    answer = tmp
    if answer[0] == '.':
        answer = answer[1:]
        if len(answer) == 0:
            answer = 'a'

    if answer[len(answer) - 1] == '.':
        answer = answer[:-1]
        if len(answer) == 0:
            answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]

    if len(answer) <= 2:
        while (len(answer) < 3):
            answer += answer[len(answer) - 1]
    return answer