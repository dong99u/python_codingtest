def solution(board):
    def is_valid(x, y, val):
        for i in range(9):
            if board[x][i] == val:
                return False
            if board[i][y] == val:
                return False

        start_x = (x // 3) * 3
        start_y = (y // 3) * 3

        for i in range(start_x, start_x + 2 + 1):
            for j in range(start_y, start_y + 2 + 1):
                if board[i][j] == val:
                    return False

        return True

    def dfs():
        # 모든 칸 확인
        for i in range(9):
            for j in range(9):
                # 빈 칸 발견!
                if board[i][j] == 0:
                    # 1~9 숫자 시도
                    for num in range(1, 10):
                        # 유효한지 확인
                        if is_valid(i, j, num):
                            # 선택!
                            board[i][j] = num

                            # 재귀: 다음 빈 칸들 채우기
                            if dfs():
                                return True  # 성공!

                            # 실패 → 백트래킹 (되돌리기)
                            board[i][j] = 0

                    # 1~9 모두 안 됨 → 이 경로 실패
                    return False

        # 빈 칸 없음 → 완성!
        return True

    dfs()
    return board

if __name__ == '__main__':
    print(solution(
        [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    ))