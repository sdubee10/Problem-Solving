import sys
from collections import defaultdict
input = sys.stdin.readline

str1 = input()
str2 = input()

dict1 = defaultdict(int)
dict2 = defaultdict(int)

n = len(str1)

for i in range(n):
    dict1[str1[i]] += 1
    dict2[str2[i]] += 1

if dict1 == dict2:
    count = 0
    for i in range(n-1, -1, -1):
        if str1[i] == str2[n-1-count]:
            count += 1
    print(n - count)
else:
    print(-1)