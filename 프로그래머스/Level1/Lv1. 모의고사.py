def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for idx, ans in enumerate(answers):
        if ans == a[idx % len(a)]:
            score[0] += 1
        if ans == b[idx % len(b)]:
            score[1] += 1
        if ans == c[idx % len(c)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)
    return answer