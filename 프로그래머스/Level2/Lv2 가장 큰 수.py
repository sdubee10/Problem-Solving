def solution(numbers):
    n = len(numbers)
    for i in range(n):
        numbers[i] = str(numbers[i])
    numbers = sorted(numbers, key = lambda x : x*3, reverse=True)
    answer = (''.join(numbers))
    return answer