def solution(numbers):
    n = len(numbers)
    for i in range(n):
        numbers[i] = str(numbers[i])
    numbers = sorted(numbers, key = lambda x : x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))