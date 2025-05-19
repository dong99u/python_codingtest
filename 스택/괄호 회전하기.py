from collections import deque

def solution(s):
    dt = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    def is_right(d):
        stack = deque()

        for elem in d:
            if elem in dt.keys():
                stack.append(elem)
            else:
                if not stack:
                    return False
                if elem == dt[stack[-1]]:
                    stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False

    def lefting(d):
        d.append(d.popleft())
        return d

    d = deque(s)
    n = len(s)

    answer = 0
    for _ in range(n - 1):
        if is_right(d):
            answer += 1
        d = lefting(d)

    return answer


if __name__ == '__main__':
    print(solution('[)(]'))