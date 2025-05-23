from collections import deque

def solution(N, K):
    d = deque([i for i in range(1, N + 1)])

    while len(d) > 1:
        for i in range(K - 1):
            d.append(d.popleft())
        d.popleft()

    return d.pop()

if __name__ == '__main__':
    print(solution(5, 2))