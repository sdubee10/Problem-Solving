"""
제곱수 정렬
문제: 오름차순 정렬되어 있는 길이가 N인 수열이 주어집니다. 수열의 원소를 제곱하여 오름차순 정열해
     출력하는 프로그램을 작성하세요.
▣ 입력설명
매개변수 nums에 N(3<=N<=100,000)길이의 수열이 주어집니다. 수열의 원소는 정수입니다.

▣ 출력설명
각 원소를 제곱하여 오름차순 정렬한 배열은 반환합니다.

▣ 매개변수 형식 1
[-4, -1, 0, 3, 10]

▣ 반환값 형식 1
[0, 1, 9, 16, 100]

▣ 매개변수 형식 2
[-7, -3, 2, 3, 11]

▣ 반환값 형식 2
[4, 9, 9, 49, 121]
"""

def solution(nums):
    answer = []
    for i in nums:
        answer.append(i ** 2)
    answer.sort()
    return answer

def solutionC(nums):
    n = len(nums)
    answer = [0] * n
    left = 0
    right = len(nums) - 1
    for i in range(n-1, -1, -1):
        if nums[left] ** 2 >= nums[right] ** 2:
            answer[i] = nums[left] ** 2
            left += 1
        elif nums[left] ** 2 <= nums[right] ** 2:
            answer[i] = nums[right] ** 2
            right -= 1

    print(answer)

def retry(nums):
    n = len(nums)
    answer = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if nums[left] ** 2 >= nums[right] ** 2:
            answer[i] = nums[left] ** 2
            left += 1
        else:
            answer[i] = nums[right] ** 2
            right -= 1
    return answer
#print(solutionC([-7, -3, 2, 3, 11]))
print(retry([-7, -3, 2, 3, 11]))
print(retry([-4, -1, 0, 3, 10]))