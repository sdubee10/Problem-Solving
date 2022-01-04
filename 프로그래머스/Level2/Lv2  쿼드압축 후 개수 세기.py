def solution(arr):
    result = [0, 0]
    n = len(arr)

    def compress(x, y, n):
        start = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != start:
                    half = n // 2
                    compress(x, y, half)
                    compress(x + half, y, half)
                    compress(x, y + half, half)
                    compress(x + half, y + half, half)
                    return
        result[start] += 1

    compress(0, 0, n)
    return result

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],
                [0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))