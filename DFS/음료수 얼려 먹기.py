def solution(n, m, arr):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] == 1:
                continue
            if visited[nx][ny]:
                continue
            dfs(nx, ny)

        return

    answer = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and arr[x][y] == 0:
                dfs(x, y)
                answer += 1

    return answer



if __name__ == '__main__':
    n, m = 4, 5

    arr = [
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]

    print(solution(n, m, arr))