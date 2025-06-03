from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        menu = []
        for order in orders:
            comb = combinations(sorted(order), c)
            menu.extend(comb)
        counter = Counter(menu)

        if (len(counter) != 0 and max(counter.values()) != 1):
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))

    return sorted(answer)



if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))