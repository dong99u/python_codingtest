def solution(board, moves):
    def exist(y):
        return any(board[x][y] != 0 for x in range(n))

    def select(y):
        for x in range(n):
            if board[x][y] == 0:
                continue
            selected = board[x][y]
            board[x][y] = 0

            return selected

    n = len(board)
    stack = []
    answer = 0

    for move in moves:
        move -= 1
        if not exist(move):
            continue
        selected = select(move)

        if stack and stack[-1] == selected:
            stack.pop()
            answer += 2
        else:
            stack.append(selected)


    return answer

if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))