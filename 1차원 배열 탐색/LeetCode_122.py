"""
문제: 122. Best Time to Buy and Sell Stock II
"""

def solution(prices):
    n = len(prices)
    maxProfit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            maxProfit += prices[i] - prices[i -1]

    return maxProfit
print(solution([7,1,5,3,6,4]))