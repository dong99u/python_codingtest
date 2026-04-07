def solution(n):
    count = 0
    while n != 0:
        if n % 2:
            count += 1
            n -= 1
        else:
            n //= 2

    return count


if __name__ == "__main__":
    print(solution(5))
    print(solution(6))
    print(solution(5000))