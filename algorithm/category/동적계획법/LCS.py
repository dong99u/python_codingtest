def solution(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]

if __name__ == '__main__':
    print(solution('ABCBDAB', 'BDCAB'))
    print(solution('AGGTAB', 'GXTXAYB'))