def solution(n, k):
    answer = 0
    while n != 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        answer += 1
    return answer


if __name__ == '__main__':
    n, k = 25, 5

    print(solution(n, k))