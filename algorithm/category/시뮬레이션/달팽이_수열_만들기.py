def solution(n):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    result = [
        [0] * n
        for _ in range(n)
    ]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    i = 1
    x = y = 0
    curr_dir = 0
    while True:
        result[x][y] = i

        if i == n * n:
            break

        nx = x + dx[curr_dir]
        ny = y + dy[curr_dir]

        if not in_range(nx, ny) or result[nx][ny] != 0:
            curr_dir = (curr_dir + 1) % 4
            nx = x + dx[curr_dir]
            ny = y + dy[curr_dir]

        x = nx
        y = ny
        i += 1

    return result

if __name__ == '__main__':
    print(solution(3))
    print(solution(4))