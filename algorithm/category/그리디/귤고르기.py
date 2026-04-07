from collections import Counter

def solution(k, tangerine):

    n = len(tangerine)
    c = Counter(tangerine)
    answer = len(c)

    sorted_c = sorted(c.items(), key=lambda x: (x[1], x[0]))

    left = n - k
    for idx, cnt in sorted_c:
        if cnt <= left:
            left -= cnt
            answer -= 1
        else:
            break

    return answer




if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
    print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
