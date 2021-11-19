# dp[i] : i번째까지 조가 잘 짜여진 최댓값
# i에서 1씩 빼면서 최댓값, 최솟값을 갱신하고 그때마다 dp[i+1] 갱신
    # 최댓값, 최솟값이 갱신되지 않으면 더 볼 필요 없음.

n = int(input())
scores = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n):
    dp[i + 1] = dp[i]
    j = i - 1
    while j >= 0 and (scores[j] < scores[i] or scores[j] > scores[i]):
        min_score = min(scores[j], scores[i])
        max_score = max(scores[j], scores[i])
        dp[i + 1] = max(dp[i + 1], dp[j] + max_score - min_score)
        print(i, "번째: ", dp)
        j -= 1
print(dp[-1])

# n = 10
# nums = [2, 5, 7, 1, 3, 4, 8, 6, 9, 3]
# # n = int(input())
# # nums = list(map(int, input().split()))
#
# # dy[n] = n번째 숫자까지의 그룹 합의 최대; n번째 숫자까지 그룹들이 있으면 그 그룹들의 max-min차이의 합계 중 최대값
# # "조가 잘 짜여진 정도" : 각 그룹의 max-min 점수 차를 다 더했을 때 그 합계가 최대가 되는 것을 찾아야 한다
# dy = [0] * n
# dy[0] = 0  # 맨 앞의 값은 자기 혼자이기 때문에 dy[0] = 0
#
# for i in range(1, n):
#     for j in range(i, -1, -1):
#         group = nums[j:i + 1]  # i가 내려오면 i에서부터(i를 포함해야하니 i+1) 그 앞의 j까지 group 짓기 (앞으로 한칸씩 증가하는 group; e.g. [5], [5,2])
#         print('group:', group)
#         print('max-min diff:', max(group) - min(group), '/ (j-1: {})'.format(j - 1), 'dy[j-1]:', dy[j - 1],
#               '/ current dy[i]:', dy[i])
#         # i부터 ~ (왼쪽으로) j까지 group이 지어지고, 이 그룹의 max, min 차이와 (한 그룹에 대한 max-min차이를 구했고, 다른 그룹의 max-min차이 최대 합계는 dy에 기록되어 있겠지?)
#         # 이 그룹 바로 전/앞 숫자(j-1)까지의 그룹 합의 최대 값(dy[j-1])을 합한 뒤, 그 합계가 현 dy[i] 값과 비교해 더 크다면/더 큰 것으로 dy[i]를 갱신하면 된다
#         # 처음엔 dy[i]값이 0으로 초기화되어 있고, 그룹에 i 숫자 자기 자신만 있어 0과 앞 dy값의 합계로 dy[i] 값이 갱신된다
#         # 이후부터 늘어나는 그룹에 위 로직대로 계산해 가고 dy[i]를 갱신해 가면 된다
#         if j == 0:  # j~i까지 그룹이 지어질 때마다 j 앞 숫자의 dy를 조회해야 하는데, j가 0아 되면(0까지 내려가면) j-1은 -1이 되기 때문에 0이 되도록 j를 1로 변경
#             j = 1
#         dy[i] = max(dy[i], dy[j - 1] + (max(group) - min(group)))
#         print('updated dy[i]:', dy[i])
#     print('dy:', dy)
#
# print('final dy:', dy)
# print('answer:', dy[n - 1])