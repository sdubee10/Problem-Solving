def solution(n, t, m, p):

    def convert(n, base):
        num = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return num[r]
        else:
            return convert(q, base) + num[r]

    answer = ""
    result = []

    # 모든 수 result에 저장
    for i in range(t * m):
        conv = convert(i, n)
        for c in conv:
            result.append(c)

    # 튜브의 답만 저장
    for i in range(p-1, t*m, m):
        answer += result[i]
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))

# 4개
# 0 1 2 3 4 5 6 7
# 0, 1, 1, 0, 1, 1, 1, 0 ,0
#
# 16개
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f , 1, 0  1 , 1, 1, 2, 1, 3 ,1 ,4 ,1 5,
# 0, 2, 4, 6, 8, a, c, e,
