def solution(board):
    answer = 0
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if board[x][y] == 0:
                            board[x][y] = -1

    for row in board:
        answer += row.count(0)

    return answer