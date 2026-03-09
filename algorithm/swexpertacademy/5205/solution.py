import sys
sys.stdin = open('input.txt')

def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= high and arr[left] <= pivot:
            left += 1

        while right > low and arr[right] >= pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[low], arr[right] = arr[right], arr[low],

    quick_sort(arr, low, right - 1)
    quick_sort(arr, right + 1, high)



t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    answer = arr[n // 2]
    print(f'#{tc} {answer}')