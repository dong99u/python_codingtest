def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]

    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, n):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i - 1][k])

    return max(dp[-1])


if __name__ == '__main__':
    print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))