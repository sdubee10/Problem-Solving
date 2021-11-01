"""
가장 높은 증가수열
문제: 길이가 N인 수열이 주어지면 이 수열에서 연속된 부분 증가수열을 찾습니다. 각 부분증가수열은
     높이가 있습니다. 증가수열의 높이란 증가수열의 첫항과 마지막항의 차를 의미합니다.

     수열이 주어지면 여러 증가수열 중 가장 높은 부분증가수열을 찾는 프로그램을 작성하세요.
     만약 수열이 [5, 2, 4, 7, 7, 3, 9, 10, 11]이 주어지면 가장 높은 부분증가수열은
     [3, 9, 10, 11]이고, 높이는 8입니다.

    이웃하는 두 수가 같을 경우 증가수열로 보지 않습니다.

▣ 입력설명
매개변수 nums에 N(3<=N<=100,000)길이의 수열이 주어집니다. 수열의 원소는 자연수입니다.

▣ 출력설명
가장 높은 연속부분증가수열의 높이를 반환합니다.

▣ 매개변수 형식 1
[5, 2, 4, 7, 7, 3, 9, 10, 11]

▣ 반환값 형식 1
8

▣ 매개변수 형식 2
[8, 12, 2, 3, 7, 6, 20, 3]

▣ 반환값 형식 2
14
"""

def solution(nums):
    answer = []
    n = len(nums)
    for i in range(n):
        tmp = []
        tmp.append(nums[i])
        while(i + 1 < n and nums[i] < nums[i+1]):
            tmp.append(nums[i+1])
            i += 1
        if len(tmp) != 1:
            answer.append(tmp)

    diff = max(answer[0]) - min(answer[0])

    for i in range(1, len(answer)):
        tmp = max(answer[i]) - min(answer[i])
        diff = max(diff, tmp)

    return diff

def solutionC(nums):
    n = len(nums)
    answer = 0
    height = 0
    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            height += (nums[i] - nums[i-1])
        else:
            answer = max(answer, height)
            height = 0
    answer = max(answer, height)
    return answer

def retry(nums):
    n = len(nums)

    answer = 0
    height = 0
    for i in range(1, n):
        if nums[i-1] < nums[i]:
            height += nums[i] - nums[i-1]
        else:
            answer = max(answer,height)
            height = 0
    answer = max(answer, height)
    return answer
print(solutionC([8, 12, 2, 3, 7, 6, 20, 3]))
print(solutionC([5, 2, 4, 7, 7, 3, 9, 10, 11]))