"""
가장 긴 수열
문제: 길이가 N인 수열이 주어지면 이 수열에서 연속으로 증가하거나, 또는 연속으로 작아지는
     부분 수열 중 가장 길이가 긴 수열을 찾는 프로그램을 작성하세요.

     만약 [5, 3, 6, 7, 9, 8, 5, 3, 1, 2]이 주어지면 우리가 찾는 가장 긴 수열은 [9, 8, 5, 3, 1]입니다.

     수열 [1, 2, 3, 3, 4, 5, 6]과 같이 같은 값이 연속으로 있는 것은 증가 또는 감소로 보지 않기
     때문에 가장 긴 수열은 [3, 4, 5, 6]이 됩니다.

▣ 입력설명
매개변수 nums에 N(3<=N<=100,000)길이의 수열이 주어집니다. 수열의 원소는 자연수입니다.

▣ 출력설명
가장 긴 수열의 길이를 반환합니다.

▣ 매개변수 형식 1
[5, 3, 6, 7, 9, 8, 5, 3, 1, 2]

▣ 반환값 형식 1
5

▣ 매개변수 형식 2
[1, 2, 3, 3, 4, 5, 6, 7, 7]

▣ 반환값 형식 2
5
"""

def solution(nums):
    up = 1
    down = 1
    maxup = 0
    maxdown=0
    n = len(nums)

    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            up += 1
        else:
            maxup = max(maxup, up)
            up = 1
        if nums[i - 1] > nums[i]:
            down += 1
        else:
            maxdown = max(maxdown, down)
            down = 1

    maxup = max(maxup, up)
    maxdown = max(maxdown, down)
    answer = max(maxup, maxdown)
    return answer

def retry(nums):
    up = 1
    down = 1
    maxup = 0
    maxdown = 0
    n = len(nums)
    for i in range(1, n):
        if nums[i-1] < nums[i]:
            up += 1
        else:
            maxup = max(maxup, up)
            up = 1
        if nums[i-1] > nums[i]:
            down += 1
        else:
            maxdown = max(maxdown, down)
            down = 1
    maxup = max(maxup, up)
    maxdown = max(maxdown, down)
    answer = max(maxdown, maxup)
    return answer

print(retry([5, 3, 6, 7, 9, 8, 5, 3, 1, 2,3,5]))
print(retry([1, 2, 3, 3, 4, 5, 6, 7, 7]))
