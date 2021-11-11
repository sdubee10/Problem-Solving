def solution(files):
    temp = []
    answer = []
    for file in files:
        digit_flag = True
        front = ""
        back = ""
        num = ""

        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
                digit_flag = False
            elif digit_flag:
                front += file[i]
            else:
                back = file[i:]
                break
        temp.append((front, num, back))
        # print(front, num, back)

    temp.sort(key = lambda x:(x[0].upper(), int(x[1])))

    for item in temp:
        tmp = "".join(item)
        answer.append(tmp)
    return answer



#["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

#["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))