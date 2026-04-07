import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, m, x, y, r, c, k):
    # d, l, r, u 순서 (사전순!)
    dxs = [1, 0, 0, -1]
    dys = [0, -1, 1, 0]
    dirs = ['d', 'l', 'r', 'u']

    result = [None]

    def get_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(curr_x, curr_y, dist, path):

        if result[0] is not None:
            return

        if dist == k:
            if curr_x == r - 1 and curr_y == c - 1:
                result[0] = path
            return

        remaining = k - dist
        min_dist = get_distance(curr_x, curr_y, r - 1, c - 1)

        if min_dist > remaining:
            return

        for i in range(4):
            nx = curr_x + dxs[i]
            ny = curr_y + dys[i]

            if not in_range(nx, ny):
                continue

            dfs(nx, ny, dist + 1, path + dirs[i])

    initial_dist = get_distance(x - 1, y - 1, r - 1, c - 1)
    if initial_dist > k or (k - initial_dist) % 2 != 0:
        return "impossible"

    dfs(x - 1, y - 1, 0, '')

    return result[0] if result[0] else "impossible"


if __name__ == '__main__':
    print(solution(3, 4, 2, 3, 3, 1, 5))
    print(solution(2, 2, 1, 1, 2, 2, 2))
    print(solution(3, 3, 1, 2, 3, 3, 4))