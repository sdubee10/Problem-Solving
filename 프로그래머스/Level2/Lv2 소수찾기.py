
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    n = len(numbers)
    for i in range(n):
        numbers[i] = int(numbers[i])

    ch = [0] * (n+1)
    res = [0] * n
    global count
    count = 0
    myset = set()
    def DFS(string, cnt):
        global count
        if cnt == n:
            if string == "":
                return
            if int(string) in myset:
                return
            if isPrime(int(string)):
                myset.add(int(string))
                count += 1
                return
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                DFS(string, cnt+1)
                newstring = string + str(numbers[i])
                DFS(newstring, cnt+1)
                ch[i] = 0
    DFS("", 0)
    return count

print(solution("011"))