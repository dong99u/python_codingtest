import sys                      # 빠른 입력을 위해 sys 사용
input = sys.stdin.readline      # input()보다 빠른 sys.stdin.readline을 input으로 사용

INF = 10**15                    # 충분히 큰 값(도달 불가능/초기 최소값 용)

def solve():
    n = int(input().strip())    # 도시(정점) 개수 n 입력
    W = [list(map(int, input().split())) for _ in range(n)]  # 비용 행렬 W[u][v] 입력
    FULL = (1 << n) - 1         # 모든 도시를 방문한 상태의 비트마스크: n비트가 전부 1
                                # 예: n=4면 FULL=1111(2)=15

    # dp[mask][u] 의미:
    # 0번 도시에서 출발해서
    # mask에 표시된 도시들을 "방문했고"
    # 현재 위치가 u일 때
    # 그때까지의 최소 비용
    dp = [[INF] * n for _ in range(1 << n)]   # mask가 0..(2^n-1) 이므로 2^n x n 테이블 생성
    dp[1 << 0][0] = 0                         # 시작 상태:
                                              # 방문집합 = {0} (1<<0), 현재도시 = 0, 비용 = 0

    for mask in range(1 << n):                # 모든 방문 상태(mask)를 작은 것부터 순회 (bottom-up)
        # 시작점 0을 포함하지 않은 mask는 애초에 "0에서 출발"이라는 정의와 맞지 않으니 스킵
        # mask & 1 은 (0번 비트가 켜져있는지) 체크하는 것. 1은 000...001
        if not (mask & 1):
            continue

        for u in range(n):                    # 현재 위치 u를 전부 시도
            # mask에 u가 포함되어 있지 않으면 "현재 u에 있다"는 상태가 성립 불가 → 스킵
            if not (mask & (1 << u)):
                continue

            cur_cost = dp[mask][u]            # 현재 상태(mask, u)의 최소 비용
            if cur_cost == INF:               # 아직 도달한 적이 없는 상태면 스킵
                continue

            # 이제 다음 도시 v로 이동해서 상태를 확장(방문 도시를 늘림)
            for v in range(n):
                # 이미 방문한 v면 다시 방문하면 안 됨 → 스킵
                if mask & (1 << v):
                    continue

                # W[u][v] == 0은 "길이 없다(이동 불가)"라는 문제 조건 → 스킵
                if W[u][v] == 0:
                    continue

                nmask = mask | (1 << v)       # v를 방문했다고 표시한 새로운 방문 상태
                cand = cur_cost + W[u][v]     # u에서 v로 가는 비용을 더한 후보 비용

                # 더 좋은(작은) 비용이면 갱신
                if cand < dp[nmask][v]:
                    dp[nmask][v] = cand

    # 여기까지 끝나면 dp[FULL][u]는:
    # "0에서 시작해서 모든 도시를 방문했고 현재 u에 있음"의 최소 비용이 됨
    # 이제 TSP는 사이클이므로 마지막에 u -> 0으로 돌아와야 함
    ans = INF                                 # 답(최소 사이클 비용) 초기화

    for u in range(n):                        # 마지막 위치 u를 전부 후보로 본다
        if dp[FULL][u] == INF:                # 모든 도시 방문 상태로 u에 도달 불가면 스킵
            continue
        if W[u][0] == 0:                      # u에서 0으로 돌아오는 길이 없으면 스킵
            continue
        # "모두 방문하고 u에 도달한 비용 + u->0 복귀 비용"의 최소를 답으로
        ans = min(ans, dp[FULL][u] + W[u][0])

    print(ans)                                # 최소 비용 출력

if __name__ == "__main__":
    solve()                                   # 메인 실행