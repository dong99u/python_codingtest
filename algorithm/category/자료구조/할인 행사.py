from collections import Counter

def solution(wants, numbers, discounts):

    def good(c1, c2):
        for key in c1:
            if key not in c2 or c2[key] < c1[key]:
                return False

        return True

    want_counter = Counter()

    for want, number in zip(wants, numbers):
        want_counter[want] = number

    answer = 0
    for start in range(len(discounts) - 9):
        discount_counter = Counter(discounts[start:start + 10])

        if good(want_counter, discount_counter):
            answer += 1

    return answer





if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))