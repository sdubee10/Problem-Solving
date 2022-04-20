import sys

input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())

matrix = [[0] * (len(word2) + 1) for _ in range(len(word1)+1)]

for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i-1] == word2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

print(matrix[-1][-1])