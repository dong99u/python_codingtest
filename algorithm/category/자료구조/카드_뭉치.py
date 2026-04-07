from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque()
    q2 = deque()

    for card in cards1:
        q1.append(card)
    for card in cards2:
        q2.append(card)

    for word in goal:
        if q1 and q1[0] == word:
            q1.popleft()
        elif q2 and q2[0] == word:
            q2.popleft()
        else:
            return 'No'

    return 'Yes'

if __name__ == '__main__':
    print(solution(["i", "drink", "water"], ["want", "to"], 	["i", "want", "to", "drink", "water"]))
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))