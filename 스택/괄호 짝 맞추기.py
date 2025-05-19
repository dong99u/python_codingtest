from collections import deque

def solution(s):
    d = deque()

    for elem in s:
        if elem == '(':
            d.append(elem)

        else:
            if len(d) == 0:
                return False
            d.pop()

    if len(d) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(solution('(())()'))