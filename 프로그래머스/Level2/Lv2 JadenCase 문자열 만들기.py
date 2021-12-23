def solution(s):
    words = s.split(" ")
    for i in range (len(words)):
        words[i] = words[i].capitalize()

    answer = " ".join(words)
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))