import sys
sys.setrecursionlimit(3000000000)

def solution(n, m, x, y, r, c, k):
    def in_range(nx, ny):
        return 0 <= nx < n and 0 <= ny < m

    def define_direction(idx):
        if idx == 0:
            return 'u'
        elif idx == 1:
            return 'd'
        elif idx == 2:
            return 'l'
        else:
            return 'r'

    def dfs(curr_x, curr_y, grid, path, length):
        if curr_x == r - 1 and curr_y == c - 1 and length == k:
            answers.append(path)
            return

        if length > k:
            return

        for idx, (dx, dy) in enumerate(zip(dxs, dys)):
            nx = curr_x + dx
            ny = curr_y + dy

            if not in_range(nx, ny):
                continue

            direction = define_direction(idx)

            grid[nx][ny] = grid[curr_x][curr_y] + 1
            dfs(nx, ny, grid, path + direction, length + 1)

    # 상하좌우 순서
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    grid = [[0] * m for _ in range(n)]
    answers = []

    dfs(x - 1, y - 1, grid, '', 0)

    answers.sort()

    if len(answers) == 0:
        return 'impossible'
    else:
        return answers[0]

if __name__ == '__main__':
    print(solution(3, 4, 2, 3, 3, 1, 5)) # dllrl
    print(solution(2, 2, 1, 1, 2, 2, 2)) # dr
    print(solution(3, 3, 1, 2, 3, 3, 4)) # impossible