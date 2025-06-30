def solution(rows, columns, queries):

    def rotate_and_find_min(x1, y1, x2, y2):
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # x1 행 움직이기
        x1y2 = grid[x1][y2]
        for y in range(y2, y1, -1):
            grid[x1][y] = grid[x1][y - 1]

        x2y2 = grid[x2][y2]
        for x in range(x2, x1 + 1, -1):
            grid[x][y2] = grid[x - 1][y2]
        grid[x1 + 1][y2] = x1y2

        x2y1 = grid[x2][y1]
        for y in range(y1, y2 - 1):
            grid[x2][y] = grid[x2][y + 1]
        grid[x2][y2 - 1] = x2y2

        x1y1 = grid[x1][y1]
        for x in range(x1, x2 - 1):
            grid[x][y1] = grid[x + 1][y1]
        grid[x2 - 1][y1] = x2y1

        min_val = float('inf')
        for y in range(y1, y2 + 1):
            min_val = min(min_val, grid[x1][y])
        for x in range(x1, x2 + 1):
            min_val = min(min_val, grid[x][y2])
        for y in range(y1, y2 + 1):
            min_val = min(min_val, grid[x2][y])
        for x in range(x1, x2 + 1):
            min_val = min(min_val, grid[x][y1])

        return min_val


    # 행렬 초기화
    grid = [[0] * columns for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            grid[i - 1][j - 1] = (i - 1) * columns + j

    answer = []
    for query in queries:
        answer.append(rotate_and_find_min(*query))

    return answer


if __name__ == '__main__':
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]