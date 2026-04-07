def solution(keyinput, board):
    def in_range(x, y):
        n = board[0] // 2
        m = board[1] // 2

        return -n <= x <= n and -m <= y <= m

    def get_dir_num(key):
        dir_num = 0
        if key == 'down':
            dir_num = 0
        elif key == 'right':
            dir_num = 1
        elif key == 'up':
            dir_num = 2
        else:
            dir_num = 3

        return dir_num

    dxs = [0, 1, 0, -1]
    dys = [-1, 0, 1, 0]

    x, y = 0, 0
    for key in keyinput:
        dir_num = get_dir_num(key)

        nx = x + dxs[dir_num]
        ny = y + dys[dir_num]

        if not in_range(nx, ny):
            continue

        x, y = nx, ny

    return [x, y]

if __name__ == "__main__":
    print(solution(["left", "right", "up", "right", "right"], [11, 11]))
    print(solution(["down", "down", "down", "down", "down"], [7, 9]))