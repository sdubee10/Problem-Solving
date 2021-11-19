import sys

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
diff = []
k -= 1

if k >= n:
    print(0)
    sys.exit()
for i in range(1, len(sensor)):
    diff.append(sensor[i] - sensor[i-1])

diff.sort()
for i in range(k, 0, -1):
    diff.pop()

print(sum(diff))