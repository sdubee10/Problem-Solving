import sys

input = sys.stdin.readline

a, b = map(int, input().split())

answer = 0
lista = []
for _ in range(a):
    lista.append(input())
for _ in range(b):
    if input() in lista:
        answer += 1
print(answer)