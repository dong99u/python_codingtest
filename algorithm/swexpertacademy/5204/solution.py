import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    global answer
    if left[-1] > right[-1]:
        answer += 1

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0

    result = merge_sort(arr)

    print(f'#{tc} {result[n // 2]} {answer}')
