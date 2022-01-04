def solution(s):
    zero = 0
    cnt = 0
    while (len(s) != 1):
        cnt += 1
        tmp = ""
        for chr in s:
            if chr == "0":
                zero += 1
            else:
                tmp += chr

        s = bin(len(tmp))[2:]
    return [cnt, zero]

print(solution("110010101001"))
print(solution("01110"))