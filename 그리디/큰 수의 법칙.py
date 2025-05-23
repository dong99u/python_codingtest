def solution(n, m, k, arr):
    arr.sort()

    max_val = arr[-1]
    max_val2 = arr[-2]

    answer = 0

    count = 0
    while count < m:
        for i in range(k):
            answer += max_val
            count += 1
        answer += max_val2
        count += 1

    return answer

if __name__ == '__main__':
    n, m, k = 5, 8, 3
    arr = [2, 4, 5, 4, 6]

    print(solution(n, m, k, arr))

