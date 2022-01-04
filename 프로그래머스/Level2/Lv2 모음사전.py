def solution(word):
    vowel = ["A", "E", "I", "O", "U"]

    global result
    result = []
    def DFS(tmp):
        global result
        if len(tmp) > 5:
            return
        result.append(tmp)
        for chr in vowel:
            DFS(tmp + chr)

    for chr in vowel:
        DFS(chr)

    result.sort()
    return result.index(word) + 1

print(solution("AAAAE"))
# print(solution("AAAE"))
# print(solution("I"))
# print(solution("EIO"))