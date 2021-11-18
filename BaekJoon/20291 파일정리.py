from collections import defaultdict
n = int(input())

files= []
for i in range(n):
    files.append(input())

clean = defaultdict(int)

for file in files:
    temp = file.split(".")
    clean[temp[1]] += 1

clean = sorted(clean.items(), key = lambda x:(x[0]))

for ext, num in clean:
    print(ext, num)