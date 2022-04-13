import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    size, s, e, k = map(int, input().split())
    stack = list(map(int, input().split()))
    stack = stack[s-1:e-1]
    stack.sort()
    # print(stack)
    print(stack[k-1])