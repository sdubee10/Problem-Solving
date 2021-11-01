"""
수열의 높이 조정
문제: N길이의 수열이 주어집니다. 수열의 높이 조정은 수열의 원소값 중 가장 큰 원소에서 1을 빼
     가장 작은 원소에 더해주는 것을 말합니다. 가장 큰 원소와 가장 작은 원소가 여러개면 그 중
     아무거나 선택하면 됩니다.

     만약 수열이 [2, 1, 3, 7, 5]라면 1회의 높이조정을 거치면 [2, 2, 3, 6, 5]가 됩니다.
     N길이의 수열이 주어지면 높이조정을 m회 한 후 가장 큰 값과 가장 작은 값을 차를 출력하는
     프로그램을 작성하세요.

▣ 입력설명
매개변수 nums에 N(3<=N<=100,000)길이의 수열이 주어집니다. 수열의 원소는 1,000을 넘지 않습니다.
매개변수 m에 높이 조정 횟수인 M(1<=M<=10,000)이 주어집니다.

▣ 출력설명
M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.
단 m회의 높이조정을 하던 중 모든 값이 같아지면 높이조정을 중단하고 0을 반환합니다.

▣ 매개변수 형식 1
[2, 1, 3, 7, 5], 2

▣ 반환값 형식 1
3

▣ 매개변수 형식 2
[69, 42, 68, 76, 40, 87, 14, 65, 76, 81], 50

▣ 반환값 형식 2
20
"""

def solution(nums, m):
    answer = 0
    for i in range(m):
        nums[nums.index(max(nums))] -= 1
        nums[nums.index(min(nums))] += 1
    return max(nums) - min(nums)

def solutionC(nums, m):
    answer = 0
    n = len(nums)
    ch = [0] * 1001
    maxH = float('-inf')
    minH = float('inf')

    for x in nums:
        ch[x] += 1
        if x > maxH:
            maxH = x
        if x < minH:
            minH = x

    for i in range(m):
        if maxH == minH:
            return 0
        if ch[maxH] == 1:
            ch[maxH] -= 1
            maxH -= 1
            ch[maxH] += 1
        else:
            ch[maxH] -= 1
            ch[maxH - 1] += 1

        if ch[minH] == 1:
            ch[minH] -= 1
            minH += 1
            ch[minH] +=1
        else:
            ch[minH] -= 1
            ch[minH + 1] += 1

    return maxH - minH

def retry(nums, m):
    answer = 0
    minH = float('inf')
    maxH = float('-inf')
    n = len(nums)
    ch = [0] * 1001

    for x in nums:
        ch[x] += 1
        if x > maxH:
            maxH = x
        if x < minH:
            minH = x
    for i in range(m):
        if maxH == minH:
            return 0

        if ch[maxH] == 1:
            ch[maxH] -= 1
            maxH -= 1
            ch[maxH] += 1
        else:
            ch[maxH] -= 1
            ch
print(solutionC([69, 42, 68, 76, 40, 87, 14, 65, 76, 81], 50))
