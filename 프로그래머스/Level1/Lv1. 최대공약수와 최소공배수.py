def gcd(n, m):
    return m if n % m == 0 else gcd(m, n % m)

def lcm(n, m):
    return n * m / gcd(n, m)

def solution(n, m):
    list = [gcd(n,m), lcm(n,m)]
    return list
