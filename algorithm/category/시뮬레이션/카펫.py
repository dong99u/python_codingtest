import math

def solution(brown, yellow):
    total_size = brown + yellow

    for vertical in range(3, int(math.sqrt(total_size) + 1)):
        if total_size % vertical == 0:
            horizontal = int(total_size / vertical)

            if brown == (horizontal + vertical) * 2 - 4:
                return [horizontal, vertical]
    return []

if __name__ == '__main__':
    print(solution(10 ,2))
    print(solution(8, 1))
    print(solution(24, 24))

