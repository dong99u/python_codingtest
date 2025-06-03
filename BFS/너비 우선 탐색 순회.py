from collections import deque

def solution(graph, start):
    q = deque([start])

    visited = [False] * 100

    adj_list = [[] for i in range(100)]

    for s, e in graph:
        adj_list[s].append(e)


    answer = []
    while q:
        popleft = q.popleft()
        if visited[popleft]:
            continue
        visited[popleft] = True


        answer.append(popleft)
        for neighbor in adj_list[popleft]:
            if not visited[neighbor]:
                q.append(neighbor)

    return answer


if __name__ == '__main__':
    print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1))
    print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))