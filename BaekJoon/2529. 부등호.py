#-------------------------------------------
#Pypy3 통과

# n = int(input())
#
# sign = list(map(str, input().split()))
#과
# small = [0] * (n + 1)
# big = [0] * (n + 1)
#
# ch = [0] * (n+2)
# res = [0] * (n+1)
# for i in range(n + 1):
#     small[i] = i
#     big[i] = 9-i
#
# def check(number, sign):
#     for i in range(n):
#         if sign[i] == "<" and number[i] > number[i+1]:
#             return False
#         if sign[i] == ">" and number[i] < number[i+1]:
#             return False
#     return True
#
# flag = False
# def DFS(L, num_list):
#     global flag
#     if flag == True:
#         return
#     if L == n + 1:
#         tmp = ""
#         for x in res:
#             tmp += str(x)
#         if check(tmp, sign) == True:
#             print(tmp)
#             flag = True
#     else:
#         for i in range(n + 1):
#             if ch[i] == 0:
#                 ch[i] = 1
#                 res[L] = num_list[i]
#                 DFS(L+1, num_list)
#                 ch[i] = 0
#
# DFS(0, big)
# ch = [0] * (n+2)
# res = [0] * (n +1)
# flag = False
# DFS(0, small)

#-------------------------------------------
#python 통
n = int(input())
sign = list(map(str, input().split()))

ch = [0] * 10
mx = ""
mn = ""

def check(i, j, k):
    if k == "<":
        return i < j
    if k == ">":
        return i > j
    return True

def DFS(cnt, string):
    global mn, mx
    if cnt == n + 1:
        if not len(mn):
            mn = string
        else:
            mx = string
        return
    for i in range(10):
        if not ch[i]:
            if cnt == 0 or check(string[-1], str(i), sign[cnt-1]):
                ch[i] = 1
                DFS(cnt+1, string + str(i))
                ch[i] = 0

DFS(0, "")
print(mx)
print(mn)