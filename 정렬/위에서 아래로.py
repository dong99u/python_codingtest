def solution(n, *arr):
    return sorted(arr, reverse=True)

if __name__ == '__main__':
    n = 3
    print(solution(n, 15, 27, 12))