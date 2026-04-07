import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, wires):
    def dfs(v):
        nonlocal count

        visited[v] = True
        count += 1

        for next in graph[v]:
            if not visited[next]:
                dfs(next)

    answer = float('inf')
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for j in range(len(wires)):
            if i == j:
                continue
            s, e = wires[j][0], wires[j][1]

            graph[s].append(e)
            graph[e].append(s)

        count = 0
        dfs(wires[i][0])

        a = n - count
        b = abs(n - a)

        answer = min(answer, abs(b - a))

    return answer

if __name__ == '__main__':
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))