from collections import deque

def in_range(n, m, x, y):
    return 0 <= x < n and 0 <= y < m

def solution(maps):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    q = deque()

    curr_x, curr_y = 0, 0
    dist[curr_x][curr_y] = 1
    visited[curr_x][curr_y] = True

    q.append((curr_x, curr_y))

    while q:
        x, y = q.popleft()

        if (x, y) == (n - 1, m - 1):
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(n, m, nx, ny):
                continue

            if visited[nx][ny]:
                continue

            if maps[nx][ny] == 0:
                continue

            visited[nx][ny] = True  # 큐에 넣을 때 visited 처리!
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))


    if dist[n - 1][m - 1] == 0:
        return -1
    else:
        return dist[n - 1][m - 1]

if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))