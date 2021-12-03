n = int(input())

words = []
for i in range(n):
    words.append(input())

dict = {}

for word in words:
    square_root = len(word) - 1
    for c in word:
        if c in dict:
            dict[c] += pow(10, square_root)
        else:
            dict[c] = pow(10, square_root)
        square_root -= 1

dict= sorted(dict.values(), reverse=True)

result = 0
m = 9
for value in dict:
    result += value * m
    m -= 1

print(result)