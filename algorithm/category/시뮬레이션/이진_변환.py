def solution(s):
    total_count = 0
    transform_count = 0
    while s != '1':
        total_count += s.count('0')
        s = s.replace('0', '')

        len_s = len(s)

        s = bin(len_s)[2:]
        transform_count += 1

    return [transform_count, total_count]


if __name__ == "__main__":
    print(solution('01110'))