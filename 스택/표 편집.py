from collections import deque

def solution(n, k, cmd):
    stack = deque()

    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    k += 1





if __name__ == '__main__':
    # print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
