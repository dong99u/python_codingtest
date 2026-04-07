def solution(arr, n):
    k = len(arr)
    result = [
        [0] * k
        for _ in range(k)
    ]

    for _ in range(n):
        for i in range(k):
            for j in range(k):
                result[j][k - 1 - i] = arr[i][j]

        arr = result

    return arr


if __name__ == "__main__":
    print(solution(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14 ,15, 16]
        ]
    , 2))