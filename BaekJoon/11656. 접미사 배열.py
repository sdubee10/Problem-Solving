word = input()

n = len(word)

dict = []
for i in range(n):
    dict.append(word[i:n+1])

dict.sort()
for word in dict:
    print(word)