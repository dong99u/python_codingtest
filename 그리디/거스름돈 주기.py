def solution(amount):
    coins = [100, 50, 10, 1]
    pointer = 0

    answer = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            answer.append(coin)

    return answer


if __name__ == '__main__':
    print(solution(123))
    print(solution(350))