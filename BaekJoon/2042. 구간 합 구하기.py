n, m, k = map(int, input().split())

nums = []
for i in range(n):
    nums.append(int(input()))

commands = []
for i in range(m + k):
    commands.append(list(map(int, input().split())))

s = 1
while(s < n):
    s *= 2

tree = [0] * (2*s)

for i in range(n):
    tree[s+i] = nums[i]

for i in range(s-1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]


def get(s, e):
    result = 0
    while s <= e:
        if s % 2 == 1:
            result += tree[s]
        if e % 2 == 0:
            result += tree[e]

        s = (s+1)//2
        e = (e-1)//2
    return result

def update(idx, val):
    while (idx > 0):
        tree[idx] += val
        idx = idx // 2


answer = []
for a, b, c in commands:
    if a == 1:
        update(s+b-1, c-tree[s+b-1])
    elif a == 2:
        answer.append(get(s+b-1, s+c-1))

for num in answer:
    print(num)