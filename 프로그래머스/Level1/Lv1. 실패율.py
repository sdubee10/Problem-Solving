def solution(N, stages):
    level = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            level[stage] = count / denominator
            denominator -= count
        else:
            level[stage] = 0
    return sorted(level, key = lambda x:level[x], reverse=True)