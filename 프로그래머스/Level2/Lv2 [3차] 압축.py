import collections

# def solution(msg):
#
#     dict = {}
#     index = 27
#     n = len(msg)
#     for i in range(26):
#         dict[chr(ord('A')+i)] = i + 1
#
#     answer = []
#     i = 0
#
#     print("pass")
#     print(msg)
#     while (i < n):
#         word = msg[i]
#         j = i
#         while (word in dict and j + 1 < n):
#             word += msg[j+1]
#             j += 1
#             if j +1 >= n:
#                 answer.append(dict[word[:-1]])
#                 break
#         if word not in dict:
#             dict[word] = index
#             index += 1
#         word = word[:-1]
#         print(dict[word], word)
#         answer.append(dict[word])
#         i = j
#         if i >= n-1:
#             answer.append(dict[word])
#             break
#         print(dict)
#         print(answer, i, word)
#     return answer


def solution(msg):
    answer = []
    dict = {}

    for i in range(26):
        dict[chr(ord('A') + i)] = i + 1

    index = 27
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dict[msg[w:c]])
            break

        if msg[w:c+1] not in dict:
            dict[msg[w:c+1]] = index
            index += 1
            answer.append(dict[msg[w:c]])
            w = c
        print(c, answer)

    return answer
print(solution("KAKAO"))
#[11, 1, 27, 15]

# print(solution("TOBEORNOTTOBEORTOBEORNOT"))
# [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]

# print(solution("ABABABABABABABAB"))
#[1, 2, 27, 29, 28, 31, 30]

