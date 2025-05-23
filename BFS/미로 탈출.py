from collections import deque

def solution(n, m, arr):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    visited = [
        [False] * m for _ in range(n)
    ]

    q = deque()

    track = [
        [0] * m for _ in range(n)
    ]
    track[0][0] = 1

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    q.append((0, 0))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue
            if arr[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue
            track[nx][ny] = track[x][y] + 1
            q.append((nx, ny))

    return track[-1][-1]



if __name__ == '__main__':
    n, m = 5, 6
    arr = [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    print(solution(n, m, arr))