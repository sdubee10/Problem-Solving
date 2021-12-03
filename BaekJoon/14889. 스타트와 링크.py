#시간 초과

# import sys
# sys.setrecursionlimit(100000)
# n = int(input())
#
# board = []
# for i in range(n):
#     board.append(list(map(int,input().split())))
#
# def DFS(idx, cnt):
#     global ans
#     if cnt == n // 2:
#         start, link = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if ch[i] and ch[j]:
#                     start += board[i][j]
#                 elif not ch[i] and not ch[j]:
#                     link += board[i][j]
#         ans = min(ans, abs(start-link))
#     else:
#         for i in range(idx, n):
#             if ch[i]:
#                 continue
#             ch[i] = 1
#             DFS(idx + 1, cnt+1)
#             ch[i] = 0
#
# ch = [0 for i in range(n)]
# ans = float('inf')
# DFS(0, 0)
# print(ans)

n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int,input().split())))

answer = float('inf')
r = n //2
res = [0] * r

def DFS(L, s):
    global answer
    if L == r:
        start, link = 0, 0
        tmp = list(set([i for i in range(1, n+1)]) - set(res))
        for i in range(r):
            for j in range(i+1, r):
                start += (nums[res[i]-1][res[j]-1] + nums[res[j]-1][res[i]-1])
                link += (nums[tmp[i] - 1][tmp[j] - 1] + nums[tmp[j] - 1][tmp[i] - 1])
        diff = abs(start - link)
        answer = min(answer, diff)
    else:
        for i in range(s, n+1):
            res[L] = i
            DFS(L+1, s+1)

ch = [0] * (n+1)
DFS(0, 1)
print(answer)