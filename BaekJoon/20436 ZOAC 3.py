
firstline = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
secondline =["a", "s", "d", "f", "g", "h", "j", "k", "l", "0"]
thirdline = ["z", "x", "c", "v", "b", "n", "m", "0", "0", "0"]

consonant = {}
vowel = {}

for i in range(3):
    if i == 0:
        for j in range(5):
            consonant[firstline[j]] = (i + 1, j)
        for j in range(5, 10):
            vowel[firstline[j]] = (i + 1, j)
    elif i == 1:
        for k in range(5):
            consonant[secondline[k]] = (i + 1, k)
        for k in range(5, 10):
            vowel[secondline[k]] = (i + 1, k)
    else:
        for m in range(4):
            consonant[thirdline[m]] = (i + 1, m)
        for m in range(4, 10):
            vowel[thirdline[m]] = (i + 1, m)

# print(consonant)
# print(vowel)

l, r = input().split()
msg = input()

time = 0
for i in range(len(msg)):
    if msg[i] in consonant:
        left = abs(consonant[l][0] - consonant[msg[i]][0])+abs(consonant[l][1] - consonant[msg[i]][1])
        time += left + 1
        l = msg[i]
    else:
        right = abs(vowel[r][0] - vowel[msg[i]][0])+abs(vowel[r][1] - vowel[msg[i]][1])
        time += right + 1
        r = msg[i]

print(time)
