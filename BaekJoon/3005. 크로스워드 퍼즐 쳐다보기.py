r, c = map(int, input().split())
board = []
dict = []
for i in range(r):
    string = input()
    board.append(list(string))
    dict.extend(string.split("#"))

for i in range(c):
    tmp = ""
    for j in range(r):
        tmp += board[j][i]
    dict.extend(tmp.split("#"))

answer = []
for word in dict:
    if len(word) >= 2:
        answer.append(word)

answer.sort()
print(answer[0])