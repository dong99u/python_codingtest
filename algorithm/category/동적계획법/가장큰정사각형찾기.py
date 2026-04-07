def solution(board):
    n = len(board)
    m = len(board[0])

    dp = [[0] * m for _ in range(n)]
    max_val = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                max_val = max(max_val, dp[i][j])

    return max_val * max_val



if __name__ == '__main__':
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))