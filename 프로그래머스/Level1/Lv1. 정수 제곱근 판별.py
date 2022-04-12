import math
def solution(n):
    answer = 0
    if math.sqrt(n) % 1 == 0:
        return int(math.sqrt(n)+1) ** 2
    return -1