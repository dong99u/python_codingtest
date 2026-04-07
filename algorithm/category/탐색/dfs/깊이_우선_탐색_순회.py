from collections import defaultdict

def solution(graph, start):
    visited = set()

    d = defaultdict(list)
    for u, v in graph:
        d[u].append(v)

    def dfs(v):
        visited.add(v)
        answer.append(v)

        for next in d[v]:
            if next not in visited:
                dfs(next)

    answer = []
    dfs(start)

    return answer



if __name__ == '__main__':
    print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
    print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))