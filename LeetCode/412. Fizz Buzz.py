def solution(n):
    fizzbuzz = "FizzBuzz"
    fizz = "Fizz"
    buzz = "Buzz"
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append(fizzbuzz)
        elif i % 3 == 0:
            result.append(fizz)
        elif i % 5 == 0:
            result.append(buzz)
        else:
            result.append(str(i))

    return result

print(solution(3))