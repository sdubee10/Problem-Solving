def solution(dartResult):
    answer = 0
    stack = [0]
    idx = 0
    while (idx < len(dartResult)):
        if dartResult[idx].isnumeric():
            num = int(dartResult[idx])
            idx += 1
            while (dartResult[idx].isnumeric() and idx < len(dartResult)):
                num = num * 10 + int(dartResult[idx])
                idx += 1
            stack.append(num)
        else:
            if dartResult[idx] == "S":
                pass
            elif dartResult[idx] == "D":
                stack.append(stack.pop() ** 2)
            elif dartResult[idx] == "T":
                stack.append(stack.pop() ** 3)
            elif dartResult[idx] == "#":
                stack.append(stack.pop() * -1)
            elif dartResult[idx] == "*":
                if len(stack) == 1:
                    stack.append(stack.pop() * 2)
                else:
                    first = stack.pop() * 2
                    second = stack.pop() * 2
                    stack.append(second)
                    stack.append(first)
            idx += 1
    return sum(stack)