"""
문제: 121. Best Time to Buy and Sell Stock

"""

def solution(prices):
    n = len(prices)

    min_num = 'inf'
    max_num = 0
    for i in range(1, n):
        min_num = min(prices[i], min_num)
        max_num = max(max_num, prices[i] - min_num)

    return max_num

print(solution([7,1,5,3,6,4]))