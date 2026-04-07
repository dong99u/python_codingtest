import sys
input = sys.stdin.readline

# 상하좌우
dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]

# 맛 조합
T = 4; C = 2; M = 1
CM = 3; TM = 5; TC = 6
TCM = 7

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

# 아침 시간엔 신앙심 + 1
def morning(B):
    for i in range(N):
        for j in range(N):
            B[i][j] += 1

# 점심 시간엔 각 그룹의 대표를 선정
# 그룹원들은 각각 신앙심 1을 대표한테 줌
def noon(B, groups):
    headers = []
    for group in groups:
        _, mi, mj = group[0] # 각 그룹 대표자의 위치
        for _, i, j in group:
            if (-B[i][j], i, j) < (-B[mi][mj], mi, mj):
                mi, mj = i, j
        headers.append((F[mi][mj], mi, mj)) # 맛조합, 대표자 좌표
        count = 0
        for _, i, j in group:
            if i == mi and j == mj: continue
            B[i][j] -= 1
            count += 1
        B[mi][mj] += count

    return headers

# 저녁 시간엔 대표자들이 신앙심을 전파함
# 전파는 아래 세 그룹 순서대로 진행
# 단일 음식 - 민트, 초코, 우유
# 이중 조합 - 초코우유, 민트우유, 민트초코
# 삼중 조합 - 민트초코우유
# 각 그룹에서 (신앙심, 행 번호 작은 순, 열 번호 작은 순)으로 나열
def evening(headers):
    ordered = []
    for flavor, i, j in headers:
        if flavor in (T, C, M):
            priority = 1
        elif flavor in (CM, TM, TC):
            priority = 2
        else:
            priority = 3
        ordered.append((priority, -B[i][j], i, j))

    ordered.sort()
    changed = set()
    for _, _, i, j in ordered:
        if (i, j) in changed:
            continue  # 전파 당한 대표자는 전파 안 함
        propagate(i, j, changed)

def propagate(i, j, changed):
    flavor = F[i][j]
    d = B[i][j] % 4
    x = B[i][j] - 1 # 간절함
    B[i][j] = 1
    ci, cj = i, j
    while True:
        ni, nj = ci + dis[d], cj + djs[d]
        if not in_range(ni, nj): break
        if F[ni][nj] == flavor: # 같은 맛이면 패스
            ci, cj = ni, nj
            continue
        y = B[ni][nj] # 전파 대상자의 신앙심
        if x > y: # 강한 전파 성공
            F[ni][nj] = F[i][j]
            x -= (y + 1)
            B[ni][nj] += 1
        else: # 약한 전파 성공
            F[ni][nj] = F[ni][nj] | F[i][j]
            B[ni][nj] += x
            x = 0
        changed.add((ni, nj))
        if x <= 0:
            break

        ci, cj = ni, nj


def grouping(F):
    def dfs(i, j, flavor, group):
        nonlocal visited
        visited[i][j] = True
        group.append((flavor, i, j))
        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if in_range(ni, nj) and not visited[ni][nj] and F[ni][nj] == flavor:
                dfs(ni, nj, flavor, group)

    visited = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group = []
                dfs(i, j, F[i][j], group)
                groups.append(group)

    return groups

def count_flavors(F, B):
    result = [0] * 8
    for i in range(N):
        for j in range(N):
            result[F[i][j]] += B[i][j]
    order = [TCM, TC, TM, CM, M, C, T]
    return [result[o] for o in order]

N, t = map(int, input().split())

# 신봉 음식
F = [[0] * N for _ in range(N)]
F_str = [list(input().strip()) for _ in range(N)]

for row_idx, row in enumerate(F_str):
    for col_idx, elem in enumerate(row):
        if elem == 'T':
            flavor = T
        elif elem == 'C':
            flavor = C
        else:
            flavor = M
        F[row_idx][col_idx] = flavor

# 신앙심
B = [list(map(int, input().split())) for _ in range(N)]

for day in range(t):
    morning(B)
    groups = grouping(F)
    headers = noon(B, groups)
    evening(headers)
    print(*count_flavors(F, B))
