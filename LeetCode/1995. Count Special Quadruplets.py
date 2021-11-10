"""
DFS를 활용한 방법이지만, 타임에러 발생함 ㅜ
def solution1(nums):
    global ch, n, res
    if len(nums) == 4:
        if nums[0] + nums[1] + nums[2] == nums[3]:
            return 1
    else:
        res = []
        n = len(nums)
        ch = [0] * n

    def DFS(L, s, nums):
        global ch, n, res
        # print("check", n, nums, ch)
        if L == n:
            if ch.count(1) == 4:
                list = []
                for i in range(n):
                    if ch[i] == 1:
                        list.append(nums[i])
                # print(list)
                res.append(list)
        else:
            for i in range(s, n):
                if ch[i] == 0:
                    ch[i] = 1
                    DFS(L + 1, i + 1, nums)
                    ch[i] = 0
                    DFS(L + 1, i + 1, nums)

    DFS(0,0, nums)
    answer = 0
    for x in res:
        if x[0] + x[1] + x[2] == x[3]:
            answer += 1
    return answer
"""

def solution(nums):
    n = len(nums)
    answer = 0
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                sum3 = nums[a] + nums[b] + nums[c]
                for d in range(c + 1, n):
                    answer += sum3 == nums[d]
    return answer

print(solution([1,2,3,6]))
print(solution([3,3,6,4,5]))
print(solution([1,1,1,3,5]))
print(solution([20,9,57,36,65,60,5,60,65,91,57,9,13,37,93]))