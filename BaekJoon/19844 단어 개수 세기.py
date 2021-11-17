#qu'est-ce qu'il mange aujourd'hui
s = input()
words = s.split()
result = []
count = 0
vowel = ["a", "e", "i", "o", "u", "h"]
check = ["c", "j", "n", "m", "t", "s", "l", "l", "d", "qu"]
for word in words:
    temp = word
    if word.count("-") >= 1:
        temp = word.split("-")
        for i in temp:
            result.append(i)
    else:
        result.append(word)

for word in result:
    n = len(word)
    for i in range(n):
        if word[i] == "'":
            if i + 1 <= n-1 and i - 1 >= 0 and word[:i] in check and word[i+1] in vowel:
                count += 2
                #print(word[:i], end = "")
                break
    else:
        count += 1
    # print("word", word, count)
# print(result)
print(count)