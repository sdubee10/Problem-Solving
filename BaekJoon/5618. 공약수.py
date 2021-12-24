import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def multiple(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

if n == 2:
    gcd = gcd(nums[0], nums[1])
else:
    temp = gcd(nums[0], nums[1])
    gcd = gcd(temp, nums[2])

result = multiple(gcd)
for i in result:
    print(i)