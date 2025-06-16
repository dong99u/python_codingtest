def solution(str1, str2):
    m = len(str1)
    n = len(str2)

    # dp 테이블 생성 (올바름)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 수정된 반복문
    for i in range(1, m + 1):  # i는 str1의 인덱스
        for j in range(1, n + 1):  # j는 str2의 인덱스
            if str1[i - 1] == str2[j - 1]:  # 같은 문자를 찾았을 때
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 다른 문자일 때
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]  # 또는 dp[-1][-1]

if __name__ == '__main__':
    print(solution('ABCBDAB', 'BDCAB'))
    print(solution('AGGTAB', 'GXTXAYB'))