def solution(k, dungeons):
    n = len(dungeons)
    ch = [0] * (n)
    global answer
    answer = -1

    def DFS(k, cnt, dungeons):
        global answer
        if cnt > answer:
            answer = cnt
        for i in range(n):
            if k >= dungeons[i][0] and ch[i] == 0:
                ch[i] = 1
                DFS(k - dungeons[i][1], cnt + 1, dungeons)
                ch[i] = 0

    DFS(k, 0, dungeons)
    return answer

