from collections import deque

def solution(board):

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    n = len(board)

    INF = float('inf')

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    q = deque()

    for d in range(4):
        nx, ny = dx[d], dy[d]
        if in_range(nx, ny) and board[nx][ny] == 0:
            cost[nx][ny][d] = 100
            q.append((nx, ny, d, 100))

    while q:
        curr_x, curr_y, prev_dir, curr_cost = q.popleft()

        if curr_cost > cost[curr_x][curr_y][prev_dir]:
            continue

        for d in range(4):
            nx = curr_x + dx[d]
            ny = curr_y + dy[d]

            if not in_range(nx, ny) or board[nx][ny] == 1:
                continue

            if d == prev_dir:
                new_cost = curr_cost + 100
            else:
                new_cost = curr_cost + 600

            if new_cost < cost[nx][ny][d]:
                cost[nx][ny][d] = new_cost
                q.append((nx, ny, d, new_cost))

    return min(cost[n-1][n-1])


if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))