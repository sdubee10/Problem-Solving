def solution(salary):
    big = max(salary)
    small = min(salary)

    salary.remove(big)
    salary.remove(small)

    n = len(salary)

    total = sum(salary)
    return round(total / n, 5)

print(solution([4000,3000,1000,2000]))