# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
#
# INF = float('inf')
#
# def get_distance(p1, p2):
#     return abs(pos[p1][0] - pos[p2][0]) + abs(pos[p1][1] - pos[p2][1])
#
# ''' 메모이제이션 적용 x
# def backtrack(prev, nxt, count, acc):
#     # 이전에 prev 체크포인트를 방문했고, nxt 체크포인트를 고려해야할 때, count개의 체크포인트를 방문했고, acc만큼 누적거리
#     if nxt == n - 1:
#         if count == n - k - 2:
#             return acc + get_distance(prev, n - 1)
#         return INF
#     if count == n - k - 2:
#         return acc + get_distance(prev, n - 1)
#
#     result = INF
#     # nxt 를 선택할 경우
#     result = min(result, backtrack(nxt, nxt + 1, count + 1, acc + get_distance(prev, nxt)))
#     # nxt를 선택하지 않을 경우
#     result = min(result, backtrack(prev, nxt + 1, count, acc))
#
#     return result
# '''

# 메모이제이션 적용 o -> 시간 초과 ( 아마 해시 연산 오버헤드 )
# def backtrack(i, remaining):
#     """
#     i번 체크포인트를 방문한 상태에서,
#     남은 건너뛰기가 remaining일 때,
#     끝까지의 최소 거리
#     """
#     state = (i, remaining)
#     if state in memo:
#         return memo[state]
#
#     if i == n - 1:
#         return 0
#
#     result = INF
#     # 다음에 실제로 방문할 체크포인트 j 선택
#     for j in range(i + 1, min(i + remaining + 2, n)):
#         skip_count = j - i - 1
#         cost = get_distance(i, j) + backtrack(j, remaining - skip_count)
#         result = min(result, cost)
#
#     memo[state] = result
#     return result
#
# n, k = map(int, input().split())
# pos = [tuple(map(int, input().split())) for _ in range(n)]
#
# memo = {}
#
# answer = backtrack(0, k)
# print(answer)

import sys
input = sys.stdin.readline

def get_distance(p1, p2):
    return abs(pos[p1][0] - pos[p2][0]) + abs(pos[p1][1] - pos[p2][1])

n, k = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')

# dp[i][j] = 체크포인트 i를 방문한 상태에서, j개를 더 건너뛸 수 있을 때, 끝까지의 최소 거리
dp = [[INF] * (k + 1) for _ in range(n)]

# 기저 조건: 마지막 체크포인트에 도착하면 추가 거리 0
for j in range(k + 1):
    dp[n - 1][j] = 0

for i in range(n - 2, -1, -1):
    for j in range(k + 1):
        # 다음에 실제로 방문할 체크포인트 t 선택
        for t in range(i + 1, min(i + j + 2, n)):
            skip_count = t - i - 1
            cost = get_distance(i, t) + dp[t][j - skip_count]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][k])