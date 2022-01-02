def solution(files):
    temp = []
    for file in files:
        num = ""
        front = ""
        back = ""
        flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
                flag = True
            elif flag == False:
                front += file[i]
            else:
                back += file[i:]
                break
        temp.append((front, num, back))
    temp.sort(key=lambda x:(x[0].upper(), int(x[1])))
    # print(temp)
    answer = []
    n = len(temp)
    for i in range(n):
        answer.append("".join(map(str, temp[i])))
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))