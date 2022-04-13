import sys

n = int(input())

for i in range(n):
    word = input()
    word = word.lower()
    # reverse = word[::-1]
    # if word == reverse:
    #     print("YES")
    # else:
    #     print("NO")

    size = len(word)
    for j in range(size//2):
        if word[j] != word[-1-j]:
            print("NO")
            break
    else:
        print("YES")

