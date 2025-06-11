from collections import defaultdict

def dfs(graph, visited, start, answer):

    visited[start] = True
    answer.append(start)
    for vertex in sorted(graph[start]):
        if not visited[vertex]:
            dfs(graph, visited, vertex, answer)
    return

def solution(graph, start):
    alpha_graph = defaultdict(list)
    v_set = set()

    for s, e in graph:
        alpha_graph[s].append(e)
        v_set.add(s)
        v_set.add(e)

    n = len(v_set)

    visited = defaultdict(bool)

    answer = []
    dfs(alpha_graph, visited, start, answer)

    return answer


if __name__ == '__main__':
    print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))