
def solution(m, n, board):
    answer = 0
    tboard = []
    for i in range(n):
        tmp_row = []
        for j in range(m-1, -1, -1):
            tmp_row.append(board[j][i])
        tboard.append(tmp_row)
    print(board)
    print(tboard)
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
