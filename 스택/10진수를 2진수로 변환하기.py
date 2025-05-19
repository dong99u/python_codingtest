from collections import deque

def solution(decimal: int):
    d = deque()

    while decimal > 0:
        d.append(decimal % 2)
        decimal //= 2

    d.reverse()
    return "".join(map(str, d))


if __name__ == '__main__':
    print(solution(12345))