import pprint

def solution(line):
    n = len(line)

    crosses = []
    for i in range(n - 1):
        for j in range(i, n):
            l, r = line[i], line[j]

            # 평행하지 않다면 교점이 있음
            if not is_parallel(l, r):
                cross = get_cross(l, r)
                if cross is not None:
                    crosses.append(cross)

    x_max = max(crosses, key=lambda a: a[0])[0]
    x_min = min(crosses, key=lambda a: a[0])[0]
    y_max = max(crosses, key=lambda a: a[1])[1]
    y_min = min(crosses, key=lambda a: a[1])[1]

    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1

    coords = [['.'] * width for _ in range(height)]

    for x, y in crosses:
        nx = x + abs(x_min) if x_min < 0 else x - x_min
        ny = y + abs(y_min) if y_min < 0 else y - y_min
        coords[ny][nx] = '*'

    answer = []
    for coord in coords:
        answer.append(''.join(coord))

    return answer[::-1]

def is_parallel(l: list, r: list) -> bool:
    a, b, e = l
    c, d, f = r

    return True if a * d - b * c == 0 else False

def get_cross(l: list, r: list) -> tuple:
    a, b, e = l
    c, d, f = r

    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)

    return (int(x), int(y)) if is_integer(x, y) else None

def is_integer(x: float, y: float) -> bool:
    return x.is_integer() and y.is_integer()

if __name__ == '__main__':
    pprint.pprint(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))