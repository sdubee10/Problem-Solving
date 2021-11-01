"""
거리 두기
문제: 현수는 영화관에 도착했습니다. 영화상영 시간보다 약간 늦은 현수는 남은 좌석을 빨리 선택하고 영화를 보려고 합니다.
     현수에게 일렬로된 좌석정보가 주어지면, 이미 앉아 있는 사람들 중 가장 가까운 사람과 최대한
     멀리 떨어져 앉을 자석을 선택해야 합니다. 여러분이 도와주세요.

▣ 입력설명
매개변수 nums에 길이가 N(3<=N<=100)인 수열을 통해 좌석의 정보가 주어집니다. 좌석정보는
1은 이미 사람이 앉은 좌석이고 0의 빈 좌석입니다.

▣ 출력설명
현수가 이미 앉은 사람과 최대한 멀리 앉을 수 있는 거리를 반환합니다.

▣ 입력예제 1
[1, 0, 0, 0, 1, 0, 0, 1, 0, 1]

▣ 출력예제 1
2

출력설명
총 10개의 좌석이 왼쪽부터 0번 좌석으로 해서 9번 좌석까지 존재한다면 현수가 2번 좌석에
앉으면 가장 가까운 사람과의 거리가 2가 됩니다. 만약 6번 좌석에 앉으면 가장 가까운 사람과의
거리는 1입니다.
"""

def solution(nums):
    answer = 0
    start = 0
    end = 0
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] == 1:
            nums[i] = 0
            count = 0
        else:
            count += 1
            nums[i] = count

    count = 0
    for i in range(n):
        if nums[(n-1)-i] == 0:
            count = 0
        else:
            count +=1
            if nums[(n-1)-i] == count:
                pass
            else:
                nums[(n-1)-i] = 0

    print(nums)
    return max(nums)


def solutionC(nums):
    answer = 0
    n = len(nums)
    dist = [0] * n
    d = 1000
    for i in range(n):
        if nums[i] == 1:
            d = 0
            dist[i] = d
        else:
            d += 1
            dist[i] = d
    d = 1000
    for i in range(n-1, -1, -1):
        if nums[i] == 1:
            d = 0
        else:
            d +=1
            dist[i] = min(dist[i], d)
    answer = max(dist)
    return answer

print(solution([1, 0, 0, 0, 1, 0, 0, 1, 0, 1]))