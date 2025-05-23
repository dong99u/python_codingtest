def solution(n, orders):
    curr_x, curr_y = 1, 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = {
        'R': 0,
        'D': 1,
        'L': 2,
        'U': 3
    }

    for order in orders:
        dir_num = direction[order]

        next_x, next_y = curr_x + dx[dir_num], curr_y + dy[dir_num]

        if not in_range(next_x, next_y):
            continue

        curr_x, curr_y = next_x, next_y

    return curr_x, curr_y

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

if __name__ == '__main__':
    n = 5
    orders = ['R', 'R', 'R', 'U', 'D', 'D']

    print(solution(n, orders))