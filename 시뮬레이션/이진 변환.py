def delete_zero(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '0':
            cnt += 1
    s = '1' * (len(s) - cnt)

    return s, cnt


def make_number(s):
    return bin(len(s))[2:]


def solution(s):
    trans_counts = 0
    zero_counts = 0

    while s != '1':
        s, cnt = delete_zero(s)
        zero_counts += cnt
        s = make_number(s)
        trans_counts += 1

    return [trans_counts, zero_counts]


if __name__ == '__main__':
    print(solution("110010101001"))