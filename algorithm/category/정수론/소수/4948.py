import sys, math
input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    arr = [i for i in range(2 * n + 1)]
    arr[0] = arr[1] = 0

    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if arr[i] == 0:
            continue
        for j in range(i + i, 2 * n + 1, i):
            arr[j] = 0

    print(len([i for i in arr[n + 1:2 * n + 1] if i != 0]))