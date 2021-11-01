"""
빈도수 구하기
문제: 길이가 N인 수열이 주어집니다. 자연수 K가 주어지면 수열의 원소 중 빈도수가 가장 많은 것
     순으로 K개를 찾아주는 프로그램을 작성하세요.

▣ 입력설명
매개변수 nums에 N(3<=N<=100,000)길이의 수열이 주어집니다. 매개변수 k에 자연수 K가 주어집니다. 수열의 원소는 정수입니다.

▣ 출력설명
빈도수가 가장 많은 K개의 원소를 배열형태로 반환합니다. 빈도수가 같은 원소가 여러개일 경우 배열의 원소의 순서는 상관없습니다.

▣ 매개변수 형식 1
[1, 1, 1, 2, 2, 3], 2

▣ 반환값 형식 1
[1, 2]

▣ 매개변수 형식 2
[3, 3, 3, 5, 1, 1, 1, 7, 2, 2], 3

▣ 반환값 형식 2
[3, 1, 2]
"""

import collections
import operator
def solution(nums, m):
    answer = []
    string = list(map(str, nums))
    string = "".join(string)

    stringHesh = collections.Counter(string)

    sorted_by_value = (sorted(stringHesh.items(), key=lambda x: x[1], reverse=True))

    for i in range(m):
        answer.append(sorted_by_value[i][0])
    print(answer)
    return True

def solutionC(nums, m):
    answer = []

    stringHash = collections.defaultdict(int)
    for num in nums:
        stringHash[num] += 1

    #sort vs. sorted
    #tmp = a.sort() -> a도 sort가 되어 있고,tmp에도 sort된 a가 저장
    #tmp = sorted(a) -> temp에만 sort된 a저장

    #0번은 key
    #1번은 value
    tmp = sorted(stringHash.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(m):
        answer.append(tmp[i][0])
    return answer

print(solutionC([3, 3, 3, 5, 1, 1, 1, 7, 2, 2], 3))