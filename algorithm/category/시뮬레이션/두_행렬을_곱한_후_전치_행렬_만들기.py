def solution(matrix1, matrix2):
    result = [
        [0] * 3
        for _ in range(len(matrix2[0]))
    ]

    for i in range(3):
        for j in range(3):
            val = 0
            for k in range(3):
                val += matrix1[i][k] * matrix2[k][j]
            result[i][j] = val

    transpose = [
        [0] * 3
        for _ in range(3)
    ]

    for i in range(3):
        for j in range(3):
            transpose[j][i] = result[i][j]

    return transpose


if __name__ == '__main__':
    print(solution(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    ))