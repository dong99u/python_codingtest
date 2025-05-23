def solution(n, m, matrix):
    answer = 0

    for row in matrix:
        answer = max(answer, min(row))

    return answer

if __name__ == '__main__':
    n, m = 3, 3
    matrix = [
        [3, 1, 2],
        [4, 1, 4],
        [2, 2, 2]
    ]

    print(solution(n, m, matrix))