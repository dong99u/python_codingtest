def solution(n, k, cmds):
    curr_idx = k + 1
    deleted = []

    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    for cmd in cmds:
        if cmd.startswith('C'):
            deleted.append(curr_idx)
            up[down[curr_idx]] = up[curr_idx]
            down[up[curr_idx]] = down[curr_idx]
            if n < down[curr_idx]:
                curr_idx = up[curr_idx]
            else:
                curr_idx = down[curr_idx]

        elif cmd.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        else:
            dir, dist = cmd.split()

            if dir == 'U':
                for _ in range(int(dist)):
                    curr_idx = up[curr_idx]

            else:
                for _ in range(int(dist)):
                    curr_idx = down[curr_idx]


    answer = ['O'] * n

    for i in deleted:
        answer[i - 1] = 'X'

    return "".join(answer)

if __name__ == '__main__':
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))