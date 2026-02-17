A = 'ABBBDAAA'
B = 'BADABBDBA'

dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

# 초기값 설정
for i in range(len(B) + 1):
    dp[i][0] = i  # B[:i] → 빈 문자열: i번 삭제
for j in range(len(A) + 1):
    dp[0][j] = j  # 빈 문자열 → A[:j]: j번 삽입

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(
                dp[i - 1][j],      # 삭제
                dp[i][j - 1],      # 삽입
            ) + 1

for row in dp:
    print(*row)

print(f"\n편집 거리: {dp[len(B)][len(A)]}")
