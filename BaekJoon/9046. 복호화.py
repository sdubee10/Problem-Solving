n = int(input())

for i in range(n):
    s = input().replace(' ', '')
    count_s = [0] * 26

    for i in s:
        count_s[ord(i) - 97] += 1

    if count_s.count(max(count_s)) > 1:
        print('?')
    else:
        print(chr(97 + count_s.index(max(count_s))))