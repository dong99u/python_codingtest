def solution(numbers: list):
    n = len(numbers)

    answer_set = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            answer_set.add(numbers[i] + numbers[j])

    return sorted(list(answer_set))


def main():
    print(solution([2, 1, 3, 4, 1]))


if __name__ == "__main__":
    main()