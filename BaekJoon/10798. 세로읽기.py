import sys

input = sys.stdin.readline

list = []
save = [['' for _ in range(15)] for _ in range(5)]

for i in range(5):
    word = input().rstrip()
    for j in range(len(word)):
        save[i][j] = word[j]

answer = ""
for i in range(15):
    for j in range(5):
        answer += save[j][i]

print(answer)