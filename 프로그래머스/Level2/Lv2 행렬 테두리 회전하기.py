def solution(rows, columns, queries):
    answer = []

    board = [[0] * columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = count
            count += 1

    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        temp = []
        left = []
        right = []
        bottom = []
        for i in range(x1, x2+1):
            if i == x1:
                for j in range(y1, y2+1):
                    temp.append(board[i][j])

            elif i == x2:
                for j in range(y1, y2 + 1):
                    bottom.append(board[i][j])
            else:
                right.append(board[i][y2])
                left.append(board[i][y1])

        temp.extend(right)
        temp.extend(bottom[::-1])
        temp.extend(left[::-1])
        answer.append(min(temp))
        print(temp)


        temp.insert(0, temp[-1])
        temp = temp[:-1]
        print(temp)

        pos = 0
        for i in range(x1, x2+1):
            if i == x1:
                for j in range(y1, y2+1):
                    board[i][j] = temp[pos]
                    pos += 1
            elif i == x2:
                for j in range(y2, y1-1,-1):
                    board[i][j] = temp[pos]
                    pos += 1
            else:
                board[i][y2] = temp[pos]
                pos += 1
        for i in range(x2-1, x1, -1):
            board[i][y1] = temp[pos]
            pos += 1

        print("=================================================")
        for i in range(rows):
            for j in range(columns):
                print(board[i][j], end = "\t")
            print("")

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))