from collections import Counter

def solution(topping):
    n = len(topping)

    a = Counter()
    b = Counter(topping)
    answer = 0
    for cut_idx in range(n - 1):
        if len(a) == len(b):
            answer += 1

        a[topping[cut_idx]] += 1
        b[topping[cut_idx]] -= 1

        if b[topping[cut_idx]] == 0:
            del b[topping[cut_idx]]

    return answer



if __name__ == "__main__":
    print(solution([1, 2, 1, 3, 1, 4, 1, 2]))