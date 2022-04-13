import sys

input = sys.stdin.readline

card = [i for i in range(21)]
for i in range(10):
    n, m = map(int, input().split())
    for j in range((m-n+1) // 2):
        card[n+j], card[m-j] = card[m-j], card[n+j]
card.pop(0)
print(card)

