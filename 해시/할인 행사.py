from collections import defaultdict

def solution(wants, numbers, discounts):
    want_dict = defaultdict(int)
    answer = 0
    for want, number in zip(wants, numbers):
        want_dict[want] = number

    for i in range(len(discounts) - 9):
        d = defaultdict(int)
        for j in range(i, i + 10):
            d[discounts[j]] += 1

        if d == want_dict:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))