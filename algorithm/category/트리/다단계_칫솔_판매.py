from collections import defaultdict

def solution(enroll, referral, seller, amount):
    d = defaultdict(str)
    profit = defaultdict(int)

    for e, r in zip(enroll, referral):
        d[e] = r

    for s, a in zip(seller, amount):
        price = a * 100
        while price > 0 and s != '-':
            profit[s] += price - price // 10
            s = d[s]
            price //= 10


    answer = []

    for e in enroll:
        answer.append(profit[e])

    return answer


if __name__ == '__main__':
    print(solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10]
    ))