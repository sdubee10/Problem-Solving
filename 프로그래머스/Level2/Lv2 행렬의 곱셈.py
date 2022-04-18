def solution(arr1, arr2):
    answer = []
    for k in range(len(arr1)):
        a = []
        for i in range(len(arr2[0])):
            n = 0
            for j in range(len(arr1[0])):
                n += arr1[k][j] * arr2[j][i]
            a.append(n)
        answer.append(a)
    return answer



print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))