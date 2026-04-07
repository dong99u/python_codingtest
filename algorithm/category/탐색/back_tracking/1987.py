import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def dfs(x, y, visited, cnt):
    global answer

    if cnt == 26:
        answer = 26
        return

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue
        if arr[nx][ny] in visited:
            continue

        visited.add(arr[nx][ny])
        dfs(nx, ny, visited, cnt + 1)
        visited.remove(arr[nx][ny])

    answer = max(answer, cnt)



r, c = map(int, input().split())

arr = [input().rstrip() for _ in range(r)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

answer = 0
visited = {arr[0][0]}
dfs(0, 0, visited, 1)

print(answer)
