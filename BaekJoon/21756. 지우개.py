import sys

input = sys.stdin.readline

n = int(input())

ch = [i for i in range(1, n+1)]

temp = []
while len(ch) != 1:
    for idx, value in enumerate(ch, 1):
        if idx % 2 == 0:
            temp.append(value)
    ch = temp
    temp = []

print(ch[0])
