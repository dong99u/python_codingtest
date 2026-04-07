def solution(prices):
    stack = [0]
    n = len(prices)

    answer = [0] * n
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer

if __name__ == '__main__':
    print(solution([1, 6, 9, 5]))
    print(solution([1, 2, 3, 2, 3]))