# 03:51
def solution(board, moves):
    h = len(board)
    stack = []
    cnt = 0
    while moves:
        now = moves.pop(0)
        for i in range(h):
            if board[i][now - 1] != 0:
                stack.append(board[i][now - 1])
                board[i][now - 1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        cnt += 2
                break

    return cnt