
word = input()
num = 0
for chr in word:
    if chr.isnumeric():
        num = num * 10 + int(chr)

cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)