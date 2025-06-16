def solution(s):
    counts = [0] * 26

    for c in s:
        counts[ord(c) - ord('a')] += 1

    sorted_str = ''

    for i in range(len(counts)):
        sorted_str += chr(ord('a') + counts[i])

    return sorted_str


if __name__ == '__main__':
    print(solution('hello'))