def solution(amount):
    coins = [1, 10, 50, 100]

    answer = []
    for coin in coins[::-1]:
        while amount >= coin:
            answer.append(coin)
            amount -= coin

    return answer


if __name__ == '__main__':
    print(solution(123))
    print(solution(350))