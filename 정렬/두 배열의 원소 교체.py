def solution(n, k, a, b):
    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]

    return sum(a)

if __name__ == '__main__':
    n, k = 5, 3
    a = [1, 2, 5, 4, 3]
    b = [5, 5, 6, 6, 5]

    print(solution(n, k, a, b))