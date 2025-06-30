def solution(n):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    matrix = [[0] * n for _ in range(n)]

    dxs = [1, 0, -1]
    dys = [0, 1, -1]

    curr_x = curr_y = 0
    dir_num = 0

    for num in range(1, (n * (n + 1)) // 2 + 1):
        matrix[curr_x][curr_y] = num

        nx = curr_x + dxs[dir_num]
        ny = curr_y + dys[dir_num]

        if not in_range(nx, ny) or matrix[nx][ny] != 0:
            dir_num = (dir_num + 1) % 3
            nx = curr_x + dxs[dir_num]
            ny = curr_y + dys[dir_num]

        curr_x = nx
        curr_y = ny

    answer = []

    for row in matrix:
        for elem in row:
            if not elem == 0:
                answer.append(elem)

    return answer

if __name__ == '__main__':
    print(solution(4))