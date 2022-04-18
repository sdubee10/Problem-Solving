def solution(arr1, arr2):
    answer = []
    h = len(arr1)
    for k in range(h):
        a = []
        for i in range(len(arr2[0])):
            n = 0
            for j in range(len(arr1[0])):
                n += arr1[k][j] * arr2[j][i]
            a.append(n)
        answer.append(a)
    return answer