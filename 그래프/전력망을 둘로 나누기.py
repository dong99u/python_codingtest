def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent):
        cnt = 1
        for child in graph[node]:
            if child != parent:
                cnt += dfs(child, node)
        return cnt

    min_diff = float('inf')
    for u, v in wires:
        graph[u].remove(v)
        graph[v].remove(u)

        cnt_a = dfs(u, v)
        cnt_b = n - cnt_a

        min_diff = min(min_diff, abs(cnt_a - cnt_b))

        graph[u].append(v)
        graph[v].append(u)

    return min_diff

if __name__ == '__main__':
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))