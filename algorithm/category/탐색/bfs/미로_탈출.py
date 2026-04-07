from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    def find_locations():
        start_x = curr_y = 0
        exit_x = exit_y = 0
        lever_x = lever_y = 0
        for i, row in enumerate(maps):
            curr_col = row.find('S')
            exit_col = row.find('E')
            lever_col = row.find('L')
            if curr_col != -1:
                start_x = i
                curr_y = curr_col
            if exit_col != -1:
                exit_x = i
                exit_y = exit_col
            if lever_col != -1:
                lever_x = i
                lever_y = lever_col

        return (start_x, curr_y, exit_x, exit_y, lever_x, lever_y)

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    def bfs(start_x, start_y, dest_x, dest_y):
        q = deque([(start_x, start_y)])

        dist = [[0] * m for _ in range(n)]

        while q:
            curr_x, curr_y = q.popleft()

            for dx, dy in zip(dxs, dys):
                nx = curr_x + dx
                ny = curr_y + dy

                if not in_range(nx, ny):
                    continue
                if dist[nx][ny] != 0:
                    continue
                if maps[nx][ny] == 'X':
                    continue

                q.append((nx, ny))
                dist[nx][ny] = dist[curr_x][curr_y] + 1

                if nx == dest_x and ny == dest_y:
                    break
        return dist[dest_x][dest_y]

    start_x, start_y, exit_x, exit_y, lever_x, lever_y = find_locations()

    distance_to_lever = bfs(start_x, start_y, lever_x, lever_y)
    distance_to_exit = bfs(lever_x, lever_y, exit_x, exit_y)

    return -1 if distance_to_lever == 0 or distance_to_exit == 0 else distance_to_exit + distance_to_lever



if __name__ == '__main__':
    print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
    print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))