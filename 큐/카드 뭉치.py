from collections import deque

def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)

    for word in goal:
        if queue1 and word == queue1[0]:
            queue1.popleft()
        elif queue2 and word == queue2[0]:
            queue2.popleft()

        else:
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # Yes