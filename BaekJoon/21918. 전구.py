import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lights = list(map(int, input().split()))
for i in range(m):
    x, l, r = map(int, input().split())
    if x == 1:
        lights[l-1] = r
    elif x == 2:
        for i in range(l, r+1):
            if lights[i-1] == 0:
                lights[i-1] = 1
            else:
                lights[i-1] = 0
    elif x == 3:
        for i in range(l, r+1):
            lights[i-1] = 0
    elif x == 4:
        for i in range(l, r+1):
            lights[i-1] = 1
print(" ".join(map(str, lights)))