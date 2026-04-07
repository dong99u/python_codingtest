def solution(N, stages):

    arr = [0] * (N + 1)

    stages.sort()

    for num in stages:
        if num > N:
            continue
        arr[num] += 1

    total_count = len(stages)
    fail_rate = {}

    for i in range(1, N + 1):
        fail_rate[i] = arr[i] / total_count
        total_count -= arr[i]

    result = sorted(fail_rate, key=lambda x: fail_rate[x], reverse=True)

    return result



if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))