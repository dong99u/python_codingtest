def solution(curr_loc):
    row, col = curr_loc[1], curr_loc[0]

    dxs = [2, 2, -2, -2, 1, -1, 1, -1]
    dys = [1, -1, 1, -1, 2, 2, -2, -2]

    count = 0
    for dx, dy in zip(dxs, dys):
        next_x = chr(ord(row) + dx)
        next_y = chr(ord(col) + dy)

        if in_range(next_x, next_y):
            count += 1
    return count


def in_range(row, col):
    return 'a' <= col <= 'h' and '1' <= row <= '8'


if __name__ == '__main__':
    print(solution('a1'))