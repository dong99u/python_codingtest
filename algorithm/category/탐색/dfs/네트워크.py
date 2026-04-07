def solution(n, computers):
    visited = [False] * n

    def dfs(v):
        visited[v] = True

        for i, computer in enumerate(computers[v]):
            if computer and not visited[i]:
                dfs(i)

    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))