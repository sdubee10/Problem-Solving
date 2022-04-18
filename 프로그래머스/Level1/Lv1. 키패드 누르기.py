# 4:36
def solution(numbers, hand):
    pad = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"],
           ["*", "0", "#"]]

    lc = (3, 0)
    rc = (3, 2)

    answer = ''
    for num in numbers:
        if num % 3 == 1:
            lc = (num // 3, 0)
            answer += 'L'
        elif num % 3 == 0 and num != 0:
            rc = ((num // 3) - 1, 2)
            answer += "R"
        else:
            if num == 0:
                loc = (3, 1)
            else:
                loc = (num // 3, 1)

            ldist = abs(lc[0] - loc[0]) + abs(lc[1] - loc[1])
            rdist = abs(rc[0] - loc[0]) + abs(rc[1] - loc[1])

            if ldist < rdist:
                lc = loc
                answer += "L"
            elif rdist < ldist:
                rc = loc
                answer += "R"
            else:
                if hand == "right":
                    rc = loc
                    answer += "R"
                else:
                    lc = loc
                    answer += "L"
    return answer