from collections import deque

def solution(board, moves):

    stack_board = []

    d = deque()
    answer = 0
    for col_idx in range(len(board[0])):
        row_stack = deque()
        for row_idx in range(len(board) - 1, -1, -1):
            if board[row_idx][col_idx] != 0:
                row_stack.append(board[row_idx][col_idx])


        stack_board.append(row_stack)

    for move in moves:
        move -= 1 # 인덱스 화

        if stack_board[move]:
            pop_val = stack_board[move].pop()

            if d:
                if d[-1] == pop_val:
                    d.pop()
                    answer += 2
                else:
                    d.append(pop_val)
            else:
                d.append(pop_val)


    return answer

if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
