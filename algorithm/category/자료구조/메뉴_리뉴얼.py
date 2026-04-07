from collections import Counter
from itertools import combinations

def solution(orders, course):

    answer = []
    for c in course:
        menu = []
        for order in orders:
            comb = combinations(sorted(order), c)
            menu += comb

        counter = Counter(menu)

        if counter and max(counter.values()) != 1:

            max_val = max(counter.values())
            for m, cnt in counter.items():
                if cnt == max_val:
                    answer.append("".join(m))

    return sorted(answer)



if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))