def solution(numbers, target):
    n = len(numbers)

    global answer
    answer = 0

    def DFS(L, total):
        global answer

        if L == n:
            if total == target:
                answer += 1
        else:
            DFS(L + 1, total + numbers[L])
            DFS(L + 1, total - numbers[L])

    DFS(0, 0)
    return answer

