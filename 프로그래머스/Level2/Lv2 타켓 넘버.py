def solution(numbers, target):
    n = len(numbers)

    global count
    count = 0


    def DFS(L, value):
        global count
        if L == n:
            if value == target:
                count += 1
            return
        else:
            DFS(L + 1, value + numbers[L])
            DFS(L + 1, value - numbers[L])

    DFS(0, 0)
    return count

print(solution([1, 1, 1, 1, 1], 3))

