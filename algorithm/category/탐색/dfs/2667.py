import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    # global count 제거
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    visited[x][y] = True
    house_count = 1  # 현재 집 카운트

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if graph[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        house_count += dfs(nx, ny)  # 재귀 결과 누적

    return house_count


n = int(input())

graph = [
    list(map(int, input().rstrip()))
    for _ in range(n)
]

visited = [[False] * n for _ in range(n)]

answers_count = 0
answers_list = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 0 or visited[x][y]:
            continue

        count = dfs(x, y)  # 반환값 받기
        answers_list.append(count)
        answers_count += 1

print(answers_count)
answers_list.sort()
for answer in answers_list:
    print(answer)

