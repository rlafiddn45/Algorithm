def solution(board, moves):
    answer = 0
    dolls = []
    for j in range(len(board[0])):
        temp = []
        for i in range(len(board) - 1, -1, -1):
            if board[i][j] != 0:
                temp.append(board[i][j])
        dolls.append(temp)
    stack = []
    for move in moves:
        n = move - 1
        if dolls[n]:
            d = dolls[n].pop()
            if stack:
                if stack[-1] == d:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(d)
            else:
                stack.append(d)
    return answer

# 0 0 0 0 0
# 0 0 1 0 3
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
