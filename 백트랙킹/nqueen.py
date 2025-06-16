def solution(n):
    grid = [[0] * n for _ in range(n)]
    answer = 0

    def valid(row_idx, col_idx):
        # 같은 열에 퀸이 있을 경우
        for i in range(n):
            if i == row_idx:
                continue
            if grid[i][col_idx] == 1:
                return False

        # 대각선에 퀸이 있을 경우
        for i in range(n):
            for j in range(n):
                if i != row_idx and j != col_idx:
                    # 오른쪽 위 → 왼쪽 아래 대각선 (/)
                    if i + j == row_idx + col_idx and grid[i][j] == 1:
                        return False
                    # 왼쪽 위 → 오른쪽 아래 대각선 (\)
                    if i - j == row_idx - col_idx and grid[i][j] == 1:
                        return False
        return True



    def dfs(row_idx):
        nonlocal answer

        if row_idx == n:
            answer += 1

        for y in range(n):
            if not valid(row_idx, y):
                continue
            grid[row_idx][y] = 1
            dfs(row_idx + 1)
            grid[row_idx][y] = 0

        return


    dfs(0)

    return answer


if __name__ == '__main__':
    print(solution(12))