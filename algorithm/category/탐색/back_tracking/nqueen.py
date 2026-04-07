def solution(n):
    board = [0] * n
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def dfs(row):
        # 종료 조건
        if row == n:
            return 1

        count = 0

        # 각 열 시도
        for col in range(n):
            # 유효성 체크 O(1)
            if (col in cols or
                    (row - col) in diag1 or
                    (row + col) in diag2):
                continue

            # 선택
            board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # 재귀
            count += dfs(row + 1)

            # 백트래킹
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return count

    return dfs(0)


if __name__ == '__main__':
    print(solution(4))