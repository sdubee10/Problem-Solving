# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# nums = list(map(int, input().split()))
#
# check = []
# def DFS(L):
#     if L == n:
#         temp = 0
#         #print("res", res)
#         for i in range(n):
#             if res[i] == 1:
#                 temp += nums[i]
#         if temp not in check:
#             check.append(temp)
#     else:
#         res[L] = 1
#         DFS(L+1)
#         res[L] = 0
#         DFS(L+1)
#
# res = [0] * n
# DFS(0)
# check.sort()
# # print(check)
#
# for num in range(1, 3000000):
#     if num not in check:
#         print(num)
#         break
#
# print(numlist[:15])


# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# answer = []
#
# def dfs(value, index):
#     if index == n:
#         return 0;
#     value += arr[index]
#     answer.append(value)
#     dfs(value, index+1)
#     value -= arr[index]
#     dfs(value, index+1)
#
# dfs(0,0)
# a = set(answer)
# for num in range(1, 2000000):
#     if num not in a:
#         print(num)
#         break

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
check = []

def DFS(value, index):
    if index == n:
        return 0
    else:
        value += nums[index]
        check.append(value)
        DFS(value, index+1)
        value -= nums[index]
        DFS(value, index+1)

DFS(0, 0)
check = set(check)
for num in range(1, 2000000):
    if num not in check:
        print(num)
        break