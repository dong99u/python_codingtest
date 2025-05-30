from collections import defaultdict


def solution(participants, completions):
    d = defaultdict(int)

    for participant in participants:
        d[participant] += 1

    for completion in completions:
        d[completion] -= 1

        if d[completion] == 0:
            del d[completion]

    for participant in participants:
        if d[participant] > 0:
            return participant

if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))