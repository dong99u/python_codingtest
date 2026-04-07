import sys
input = sys.stdin.readline

def check_bingo():
    """전체 빙고 개수를 세는 함수"""
    cnt = 0

    # 가로줄 체크
    for i in range(5):
        if all(visited[i][j] for j in range(5)):
            cnt += 1

    # 세로줄 체크
    for j in range(5):
        if all(visited[i][j] for i in range(5)):
            cnt += 1

    # 주 대각선 체크 (i == j)
    if all(visited[i][i] for i in range(5)):
        cnt += 1

    # 역 대각선 체크 (i + j == 4)
    if all(visited[i][4-i] for i in range(5)):
        cnt += 1

    return cnt

n = 5
board = [list(map(int, input().split())) for _ in range(n)]

bingo = 0

visited = [[False] * n for _ in range(n)]

answer = 0
found = False

pos = {}

for i in range(n):
    for j in range(n):
        pos[board[i][j]] = (i, j)

for k in range(n):
    arr = list(map(int, input().split()))
    for idx, val in enumerate(arr):
        i, j = pos[val]
        visited[i][j] = True

        if check_bingo() >= 3:
            answer = 5 * k + (idx + 1)
            found = True
            break

    if found:
        break

print(answer)