n = input().rstrip()

tmp = ''
m = input().rstrip()
for chr in n:
    if not chr.isnumeric():
        tmp += chr

if m in tmp:
    print(1)
else:
    print(0)