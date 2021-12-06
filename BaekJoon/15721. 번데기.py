import sys

input = sys.stdin.readline

n = int(input())
t = int(input())
k = int(input())

queue = []
call = 2
flag = False
while True:
    queue += [0, 1, 0, 1]
    for i in range(call):
        queue.append(0)
    for i in range(call):
        queue.append(1)

    size = len(queue)
    count = 0
    for i in range(size):
        if queue[i] == k:
            count += 1
            if count == t:
                answer = i
                flag = True
                break
    if flag:
        break
    call += 1
print(answer % n)
