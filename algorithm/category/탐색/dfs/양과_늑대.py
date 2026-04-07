def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    answer = 0

    for u, v in edges:
        tree[u].append(v)

    def dfs(v, sheep_cnt, wolf_cnt, available):
        nonlocal answer

        if info[v] == 0:
            sheep_cnt += 1
        else:
            wolf_cnt += 1

        if wolf_cnt >= sheep_cnt:
            return

        answer = max(answer, sheep_cnt)

        available = available | set(tree[v])
        available.discard(v)

        for next in available:
            dfs(next, sheep_cnt, wolf_cnt, available)

    dfs(0, 0, 0, set())

    return answer


if __name__ == '__main__':
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))