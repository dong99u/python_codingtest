def solution(dirs):
    def is_range(x, y):
        return 0 <= x < 11 and 0 <= y < 11

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dir_num = 0

    x, y = 5, 5
    answer = set()

    for dir in dirs:
        if dir == 'U':
            dir_num = 0
        elif dir == 'R':
            dir_num = 1
        elif dir == 'D':
            dir_num = 2
        elif dir == 'L':
            dir_num = 3

        nx, ny = x + dx[dir_num], y + dy[dir_num]

        if not is_range(nx, ny):
            continue

        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        x, y = nx, ny

    return len(answer) / 2




