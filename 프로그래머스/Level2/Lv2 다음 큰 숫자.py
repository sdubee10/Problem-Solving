def solution(n):
    bin1 = str(bin(n))[2:]
    next = n+1
    bin2 = str(bin(next))[2:]

    while (bin1.count("1") != bin2.count("1")):
        next += 1
        bin2 = str(bin(next))[2:]
    return next

print(solution(78))
print(solution(15))