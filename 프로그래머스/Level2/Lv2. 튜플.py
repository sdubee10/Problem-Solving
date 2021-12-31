def solution(s):
    s = s.replace("{{", "")
    s = s.replace("},{", " ")
    s = s.replace("}}", "")

    result = []
    l = list(map(str, s.split()))
    l.sort(key = len)

    for i in l:
        i = i.replace(",", " ")
        for num in i.split(" "):
            if int(num) not in result:
                result.append(int(num))
    result = list(result)
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))