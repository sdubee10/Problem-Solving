import sys

input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())

table = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

answer = ''
for i in range(1, len(word1)+1):
    for j in range(1, len(word2) + 1):
        if word1[i-1] == word2[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

print(table[-1][-1])
y = len(word1)
x = len(word2)

while x > 0 and y > 0:
    if table[y-1][x] == table[y][x]:
        y -= 1
    elif table[y][x-1] == table[y][x]:
        x -= 1
    else:
        answer += word2[x-1]
        x -= 1
        y -= 1

print(answer[::-1])
