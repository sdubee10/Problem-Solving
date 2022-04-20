import sys
input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())
word3 = list(input().rstrip())

table = [[[0] * (len(word3)+1) for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

for k in range(1, len(word1) + 1):
    for i in range(1, len(word2)+1):
        for j in range(1, len(word3) + 1):
            if word2[i-1] == word3[j-1] and word2[i-1] == word1[k-1]:
                table[k][i][j] = table[k-1][i-1][j-1] + 1
            else:
                table[k][i][j] = max(table[k][i - 1][j], table[k][i][j-1], table[k-1][i][j])
print(table[-1][-1][-1])