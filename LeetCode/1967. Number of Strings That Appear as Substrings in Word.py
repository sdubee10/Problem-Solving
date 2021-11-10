"""
## DFS로 경우의 수 찾아면 안됨!!!!!!!! ㅜㅜ

def solution(patterns, word):
    result = []
    answer = 0
    n = len(word)
    ch = [0] * (n)

    def DFS(L, s):
        if L == n:
            tmp = ""
            for i in range(n):
                if ch[i] == 1:
                    tmp += word[i]
            if tmp not in result:
                result.append(tmp)
            print(result)
        else:
            for i in range(s, n):
                if ch[i] == 0:
                    ch[i] = 1
                    DFS(L + 1, i+1)
                    ch[i] = 0
                    DFS(L + 1, i+1)

    DFS(0, 0)
    for pattern in patterns:
        if pattern in result:
            answer += 1
    return answer
"""

def solution(patterns, word):
    answer = 0
    for pattern in patterns:
        if pattern in word:
            answer += 1
    return answer

# print(solution(["a","abc","bc","d"], "abc"))
# print(solution(["a","b","c"], "aaaaabbbbb"))
# print(solution(["a","a","a"], "ab"))
# print(solution(["glgpqusg","qsyrgdelg","akcsg","e","fnmi","gzqsyrgdelg","lapwypxrmaydjr","s","iwig"], "numiwigzqsyrgdelgxs"))
